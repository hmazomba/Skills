# Godot MCP provider installation

Verified upstream repositories (2026-11-09):
- NPGameDev Godot MCP Toolkit: https://github.com/NPGameDev/godot-mcp-toolkit
- NPGameDev bridge: https://github.com/NPGameDev/godot-mcp-server
- Store entry: https://store.godotengine.org/asset/npgamedev/godot-mcp-toolkit/
- IvanMurzak Godot-MCP: https://github.com/IvanMurzak/Godot-MCP
- Godot Asset Library asset 5245: https://godotengine.org/asset-library/asset/5245
- Coding-Solo godot-mcp: https://github.com/Coding-Solo/godot-mcp

IMPORTANT: Godot asset 5245 is IvanMurzak; NPGameDev store entry is DIFFERENT.

## A. NPGameDev (recommended default)

Requirements: Godot >=4.2, Node.js >=22, desktop OS (Linux/macOS/Windows). Use pinned version from repository release. Latest checked release: v1.1.2 at 2026-11-09; recheck prior to changing it.

1. In target game project root, run `python3 /path/to/Skills/gamedev/godot-prompt-optimizer/scripts/install_mcp_toolkit.py --project /absolute/project/path --dry-run`. On Windows use `py -3`.
2. Run again without `--dry-run`. Helper downloads **official** release archive, validates archive members against traversal/symlinks, extracts only `addons/godot_mcp_toolkit`, and updates `.mcp.json` while preserving other server entries. It refuses existing addon unless `--upgrade` is explicitly supplied. Backup directory before upgrade.
3. Open Godot. Project Settings > Plugins > Godot MCP Toolkit > Active. Do not edit `project.godot` beneath live editor.
4. Verify Godot Output contains `[MCPServer] listening on 127.0.0.1:6550` or nearby port 6550–6560.
5. Reconnect/restart MCP client; perform read-only tool probe (scene tree or project settings). Inspect tool discovery; provider may dynamically enable additional tool groups.
6. For Claude Code, preferred editor menu is Project > Tools > MCP Toolkit > Write .mcp.json, which pins compatible bridge version. If installer already supplied config, compare it with generated pin before overriding.
7. Bridge command by default: `npx -y @npgamedev/godot-mcp-server`. Windows manual configuration if npx spawn fails: `cmd /c npx -y @npgamedev/godot-mcp-server`.
8. For project-only JSON configuration, example (not universal across MCP clients):

```json
{
  "mcpServers": {
    "godot-mcp-toolkit": {
      "command": "npx",
      "args": ["-y", "@npgamedev/godot-mcp-server"]
    }
  }
}
```

Toolkit editor listens on local WebSocket. Session authentication uses generated token; do not publish editor ports, logs, tokens, or credentials. Plugin checks GitHub for updates by default (opt-out via `mcp_toolkit/updates/check_for_updates`), so it is not *strictly offline* even though game data stays local. For offline use install npm bridge ahead of time, pin versions, and disable checks.

`GODOT_MCP_READ_ONLY=1` hides mutating tools in bridge when enabled; useful for audits, not for building games.

When upgrading, editor closed, backup project/addon, then remove old addon before extract to avoid stale `.uid` sidecars. Script supports `--upgrade` with backup. Existing config entry is never replaced unless `--replace-config` used.

## B. IvanMurzak (Asset Library 5245)

Requirements: Godot 4.3+ **.NET/C# editor**, .NET 8 SDK, Node.js/npm for `godot-cli`, C# project `.csproj`. This is an advanced integration potentially using remote `ai-game.dev` service. Only log in or use cloud mode after user choice; self-host alternative exists.

Official CLI flow:

```bash
npm install -g godot-cli
godot-cli install-plugin ./MyGodotProject
godot-cli login
godot-cli setup-mcp claude-code ./MyGodotProject
godot-cli open ./MyGodotProject
godot-cli wait-for-ready ./MyGodotProject
```

`godot-cli create-project --dotnet ./MyGodotProject` can scaffold a **new** .NET project, but never convert existing project without explicit user request. `godot-cli login` uses cloud device auth; omit for planned self-hosted install. User may choose Godot Asset Library installer with subsequent NuGet setup: follow official upstream README and CLI docs, don't assume copying addon alone is enough. Validate credentials are not committed. Do not call on GDScript-only project.

## C. Coding-Solo CLI MCP

Requirements: Godot installed, Node.js >=18, MCP-aware client.

Claude Code:
```bash
claude mcp add godot -- npx @coding-solo/godot-mcp
```

Optionally `GODOT_PATH=/path/to/godot`. This server exposes `get_godot_version`, `list_projects`, `get_project_info`, `launch_editor`, `run_project`, `get_debug_output`, `stop_project`, `create_scene`, `add_node`, `load_sprite`, `export_mesh_library`, `save_scene`, `get_uid`, `update_project_uids` (Godot UID tools need 4.4+). It does not advertise script-editing or screenshot tools in its current list; use separate coding/filesystem access.

## Cross-provider guardrails

- Inspect actual MCP tool list before mentioning concrete operations.
- Prefer one provider as active writer. Two providers can create concurrent-editor/file races.
- Inspect `.mcp.json` and client-specific settings; never replace whole config when appending.
- Work inside project, back up before upgrade, avoid auto-launching untrusted downloaded installers.
- Get consent for cloud login, global packages, destructive cleanup or overwrites.
- Report what was verified independently from what user must complete in editor.
