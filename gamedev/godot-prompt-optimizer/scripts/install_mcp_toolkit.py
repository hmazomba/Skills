#!/usr/bin/env python3
"""Install NPGameDev Godot MCP Toolkit addon into an existing Godot project.

Python 3.9+, standard library only. Does not activate plugin or start Godot.
Downloads official GitHub release ZIP; preserves other MCP server config entries.
"""
import argparse
import io
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from datetime import datetime, timezone

VERSION = "1.1.2"
BASE_URL = "https://github.com/NPGameDev/godot-mcp-toolkit/releases/download"
ADDON_NAME = "godot_mcp_toolkit"
SERVER_NAME = "godot-mcp-toolkit"
# Godot MCP Toolkit needs Node.js >=22. Check Node version separately.
MCP_ENTRY = {"command": "npx", "args": ["-y", "@npgamedev/godot-mcp-server"]}


def fail(message):
    raise RuntimeError(message)


def safe_members(zf):
    """Return (zip entry, relative path under addon) for addon files only."""
    result = []
    for item in zf.infolist():
        path = PurePosixPath(item.filename.replace("\\", "/"))
        parts = path.parts
        # No paths with .., empty fields, absolute paths, drive prefixes.
        if path.is_absolute() or ".." in parts or any(":" in p for p in parts):
            fail(f"Unsafe ZIP member: {item.filename}")
        if item.is_dir():
            continue
        # Reject Unix symlinks (can escape extracted directory).
        if (item.external_attr >> 16) & 0o170000 == 0o120000:
            fail(f"ZIP member is symlink: {item.filename}")
        try:
            idx = next(i for i in range(len(parts) - 1)
                       if parts[i:i + 2] == ("addons", ADDON_NAME))
        except StopIteration:
            continue
        relative = Path(*parts[idx + 2:])
        if not relative.parts:
            continue
        result.append((item, relative))
    if not result or not any(str(p) == "plugin.cfg" for _, p in result):
        fail("Archive lacks addons/godot_mcp_toolkit/plugin.cfg")
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--project", required=True, help="Existing Godot project directory")
    p.add_argument("--version", default=VERSION, help="Official release version, e.g. 1.1.2")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--upgrade", action="store_true", help="Back up and replace existing addon")
    p.add_argument("--replace-config", action="store_true", help="Replace existing Godot MCP Toolkit entry only")
    args = p.parse_args()

    root = Path(args.project).expanduser().resolve()
    if not (root / "project.godot").is_file():
        fail(f"project.godot missing in {root}")
    addon = root / "addons" / ADDON_NAME
    config_path = root / ".mcp.json"

    if addon.exists() and not args.upgrade:
        fail(f"{addon} already exists. Use --upgrade to back up and replace it.")
    if addon.is_symlink():
        fail("Refusing to replace symlink addon folder.")
    if config_path.exists() and config_path.is_symlink():
        fail("Refusing to modify symlink .mcp.json.")

    if config_path.exists():
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as ex:
            fail(f"Existing .mcp.json invalid: {ex}")
        if not isinstance(config, dict):
            fail(".mcp.json must contain an object")
    else:
        config = {}
    servers = config.setdefault("mcpServers", {})
    if not isinstance(servers, dict):
        fail(".mcp.json mcpServers must be an object.")
    if SERVER_NAME in servers and servers[SERVER_NAME] != MCP_ENTRY and not args.replace_config:
        fail("Existing godot-mcp-toolkit config differs. Use --replace-config to overwrite its entry.")
    servers[SERVER_NAME] = MCP_ENTRY

    version = args.version.strip().lstrip("v")
    if not version or any(ch not in "0123456789." for ch in version):
        fail("Version must contain digits/dots only, e.g. 1.1.2")
    url = f"{BASE_URL}/v{version}/godot-mcp-toolkit-{version}.zip"
    print(f"Project: {root}")
    print(f"Addon: {addon}")
    print(f"Release: {url}")
    print(f"MCP config: {config_path}")
    if args.dry_run:
        print("DRY RUN. No files changed. Network download skipped.")
        return

    # Download into memory with bounded size, then inspect before writing to project.
    req = urllib.request.Request(url, headers={"User-Agent": "godot-prompt-optimizer/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        data = response.read(100 * 1024 * 1024 + 1)
    if len(data) > 100 * 1024 * 1024:
        fail("Release archive too large (>100 MiB).")
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        selected = safe_members(zf)
        with tempfile.TemporaryDirectory(prefix="godot-mcp-") as temp:
            staged = Path(temp) / ADDON_NAME
            staged.mkdir()
            # Extract only selected addon files, with collision protection.
            seen = set()
            for info, relative in selected:
                k = str(relative).lower()
                if k in seen:
                    fail(f"Duplicate/case-colliding ZIP path: {relative}")
                seen.add(k)
                if info.file_size > 20 * 1024 * 1024:
                    fail(f"Unusually large addon file: {relative}")
                target = staged / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(info) as source, target.open("wb") as dest:
                    shutil.copyfileobj(source, dest, 1024 * 1024)
            if not (staged / "plugin.cfg").is_file():
                fail("Staged addon missing plugin.cfg")
            addon.parent.mkdir(parents=True, exist_ok=True)
            if addon.exists():
                stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
                backup = addon.with_name(f"{ADDON_NAME}.backup-{stamp}")
                if backup.exists():
                    fail(f"Backup already exists: {backup}")
                addon.rename(backup)
                print(f"Backup: {backup}")
            # Move staging into place before writing .mcp.json.
            shutil.move(str(staged), str(addon))

    # Atomic .mcp.json replacement, backup originals before changing.
    if config_path.exists():
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup_config = config_path.with_name(f".mcp.json.backup-{stamp}")
        if backup_config.exists():
            fail(f"Backup already exists: {backup_config}")
        shutil.copy2(config_path, backup_config)
        print(f"Config backup: {backup_config}")
    fd, tempname = tempfile.mkstemp(prefix=".mcp.json.", dir=str(root))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tempname, config_path)
    finally:
        if os.path.exists(tempname):
            os.unlink(tempname)
    print("Installed addon and updated .mcp.json.")
    print("Next: open Godot; Project Settings > Plugins > Godot MCP Toolkit > Active.")
    print("Next: verify MCP dock listening, restart MCP client, then run read-only probe.")
    print("NOTE: Bridge requires Node.js >=22; verify node --version.")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError, zipfile.BadZipFile) as err:
        print(f"ERROR: {err}", file=sys.stderr)
        sys.exit(1)
