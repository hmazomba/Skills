# Godot prompt examples

## Rough input: "Build a 2D platformer with double jump and enemies"

### System Role
Senior Godot 4 GDScript 2D engineer with MCP-assisted validation.

### Brief
Build a playable side-scrolling 2D platformer: horizontal movement, jump, one mid-air double jump, grounded reset, patrol enemy, health and respawn.

### Environment
Godot 4.x installed version must be verified. GDScript default, desktop keyboard, placeholder art. NPGameDev MCP Toolkit if connected.

### Architecture
`scenes/Main.tscn`: `Node2D` root with `TileMapLayer` (Godot version-dependent), Player (`CharacterBody2D`), enemy nodes, `CanvasLayer` HUD; player script handles `velocity` and `move_and_slide()`; input actions `move_left`, `move_right`, `jump`; camera follow `Camera2D`; damage from collision groups/layers.

### Acceptance
Character can move left/right, jump twice but not thrice, touching ground resets jumps; enemy patrols and damages once per cooldown; death respawns; no parser/runtime errors; keyboard input and collisions tested.

### Execution
Read project; write spec; implement slice; test input and collisions; inspect logs; capture screenshot if MCP supports it; report verified outcomes.

## Rough input: "Make racing game like classic mountain touge"

Optimize first: vehicle handling (arcade vs simulation), gravity/terrain and drift, camera, track spline/mesh source, checkpoints, AI traffic, target FPS, controls, physics tick, scene composition, lightweight assets and acceptance. Do not copy copyrighted tracks or assets; create original references or use licensed user-provided material.

## Bug input: "Player falls through floor"

Diagnose: layer/mask mismatch, missing CollisionShape, disabled collision, invalid scale, unsuitable physics body movement, inappropriate continuous collision settings, floor shape geometry. Tell agent inspect actual scene tree, layer bits and physics debug before changing code. Fix smallest verified cause and replay test.
