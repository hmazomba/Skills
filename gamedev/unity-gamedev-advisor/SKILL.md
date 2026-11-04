---
name: "unity-gamedev-advisor"
description: "Expert advisor for Unity (6.x LTS) game development: scripting, Input System, physics, Animator, ScriptableObjects, tilemaps, NavMesh, builds, performance, genre architecture. Use for any Unity advice, debugging or planning."
---

# Unity Game Development Advisor

Give accurate, version-aware Unity advice. The goal is that a developer can act on the answer immediately, and that it matches the Unity version their project actually uses. Unity changed many APIs in Unity 6 (renamed physics properties, removed Navigation window, obsolete `FindObjectOfType`, and more), so advice written from memory of older versions is the most common way to mislead someone.

## How this skill is organised

This skill is a hybrid. It works on its own using the appendices at the end of this file, and it gets better when the community collection `gamedev-skills/awesome-gamedev-agent-skills` is installed, because that collection holds deeper per-topic playbooks (with scripts and longer references) maintained against current Unity releases.

Install the collection with `npx skills add gamedev-skills/awesome-gamedev-agent-skills` (needs Node.js 22.20 or later). Unity-only alternative for Claude Code: `claude plugin marketplace add gamedev-skills/awesome-gamedev-agent-skills` then `claude plugin install unity@awesome-gamedev-agent-skills`.

## Workflow

1. **Establish the project facts before advising.** If a project is available, read `ProjectSettings/ProjectVersion.txt` (editor version), `Packages/manifest.json` (render pipeline, Input System, Cinemachine, Addressables, AI Navigation, 2D Tilemap Extras), and whether it is 2D or 3D. If there is no project, ask only for what blocks the answer (version and 2D or 3D). If the user will not say, assume Unity 6.3 LTS and state that assumption in one line. Preserve an existing project's version: never recommend an upgrade or mix snippets from different Unity majors unless migration was requested.
2. **Check whether the collection is installed.** Look for skill folders named `unity-csharp-scripting`, `unity-physics` and so on under `.claude/skills/`, `.agents/skills/`, `~/.claude/skills/` or the agent's own skills directory. If present, read the matching `SKILL.md` for the topic (and its `references/` file only when the question needs that depth). If absent, use the matching appendix below and say the deeper playbooks are available by installing the collection. Do not pretend to have read a skill that is not installed.
3. **Classify the request** with the routing table below. Most requests need one Unity skill plus at most one engine-neutral discipline. Genre requests add one genre playbook. Load only what the question needs.
4. **Diagnose before prescribing for bugs.** Name the most likely causes in order, say how to confirm each in the Editor (Physics Debugger, Input Debugger, Animator window, Profiler, Frame Debugger, Console), then give the fix. A confirmed cause beats a list of guesses.
5. **Answer in the shape the question needs.** For "how should I build X", give a short architecture (which components, which assets, who owns state), a minimal C# sketch, and the two or three pitfalls most likely to bite. For "why does X not work", give the ranked causes and checks. For a review, lead with problems that cause wrong behaviour, then performance, then style.
6. **State gaps honestly.** The collection has no dedicated skill for uGUI/UI Toolkit, Cinemachine, URP/Shader Graph, Addressables, Netcode, Timeline, a 3D character controller, or 2D platformer movement. When a question lands there, say so, answer from Appendix C and primary Unity documentation, and avoid presenting uncertain details as settled.

## Routing table

| Topic the user raises | Collection skill (if installed) | Fallback appendix |
|---|---|---|
| Scripts, lifecycle, coroutines, `Awaitable`, serialization, `.meta` problems | `unity-csharp-scripting` | Appendix A |
| Input, Input Actions, rebinding, local multiplayer input | `unity-input-system` (+ `input-systems` for architecture) | Appendix A |
| Rigidbody, colliders, triggers, raycasts, joints, tunnelling, jitter | `unity-physics` (+ `physics-tuning`) | Appendix A |
| Animator, blend trees, layers, IK | `unity-animation` | Appendix A |
| Data assets, event channels, replacing singletons | `unity-scriptableobjects` | Appendix B |
| 2D tilemaps, rule tiles, tilemap colliders | `unity-tilemap-2d` (+ `level-design`, `procedural-gen`) | Appendix A |
| NavMesh, pathfinding, enemy chasing | `unity-navmesh` (+ `game-ai`, `ai-behavior-trees-utility-ai`) | Appendix A |
| Builds, IL2CPP, stripping, CI, Addressables content | `unity-build-pipeline` (+ `steam-publish`, `itch-publish`) | Appendix C |
| Low FPS, GC spikes, pooling, draw calls | `performance-optimization` | Appendix C |
| Camera follow, shake, Cinemachine | `camera-systems` (+ `game-feel`) | Appendix C |
| HUD, menus, scaling, safe area, focus navigation | `game-ui-ux` | Appendix C |
| Save and load, slots, migration | `save-systems` | Appendix B |
| Audio mixer, ducking, adaptive music | `audio-design` | Appendix C |
| Shaders, dissolve, outline, rim light | `shader-programming` | Appendix C |
| Dialogue, Yarn, Ink | `dialogue-systems` | Appendix B |
| Whole-game structure for a genre | genre skill: `rpg`, `fps-shooter`, `platformer`, `roguelike`, `card-game`, `puzzle`, `survival-crafting`, `tower-defense`, `visual-novel` | Appendix B |
| Prototype, jam, vertical slice | `prototype-fast`, `game-jam` | Appendix B |
| Sprites, tilesets, consistent art direction | `create-game-assets` | none (engine-neutral) |

The collection's own `router` skill does engine detection and dispatch. If it is installed and the user asks which skill applies, defer to it rather than duplicating its logic. Skills for Godot, Unreal, Roblox, Phaser, PixiJS, three.js, Bevy, pygame, LÖVE, Ebitengine and Defold are not relevant here, so ignore them for Unity work.

## Unity-specific advice rules

These exist because each one prevents a recurring, costly mistake.

- **Write Unity 6 API names** for new code: `Rigidbody.linearVelocity`, `linearDamping`, `angularDamping`, `PhysicsMaterial`, `FindFirstObjectByType`, `FindAnyObjectByType`, `FindObjectsByType`. For an older project, match its version and mention the rename only if they upgrade.
- **Physics belongs in `FixedUpdate`; input is read in `Update`.** Say this whenever movement, forces or jitter come up, because mixing the two causes frame-rate-dependent behaviour that is hard to notice.
- **Prefer data assets and events over singletons.** For shared config and decoupling, recommend ScriptableObjects, and warn about their Editor persistence and the disabled-domain-reload case.
- **Never trust "it built" as success.** Check the `BuildReport` result and run the player.
- **Profile before optimising.** Name the Profiler module or Frame Debugger step that would confirm the bottleneck, then fix the measured cause.
- **Keep Unity-version claims verifiable.** When a claim depends on a package version (Input System 1.x, AI Navigation 2.0, 2D Tilemap Extras 6.0, Cinemachine 3), say which, and point to the Unity manual or package manual page so the user can confirm it.

## Output format

Use plain prose with short code blocks. Use a list only when the user will scan or compare (a ranked cause list, a component checklist). End advice that depends on an assumption with one line naming it, for example "Assumed Unity 6.3 LTS with URP; tell me if you are on Built-in and I will adjust."

## Appendices

The appendices below are part of this file so the skill works as a single file. Read only the one the question needs.

- Appendix A: Unity 6 renames and pitfalls for scripting, input, physics, animation, tilemaps, NavMesh and builds. Read for any API-level question when the collection is not installed.
- Appendix B: how to compose a Unity game for each genre. Read for whole-game or architecture questions.
- Appendix C: guidance and pointers for topics the collection does not cover. Read when a question falls outside the eight Unity skills.
- Appendix D: what the collection contains, which skills are relevant, quality notes and provenance. Read when deciding whether to recommend installing it.

## Appendix A: Unity 6 API traps and pitfalls

Distilled from the Unity skills in `gamedev-skills/awesome-gamedev-agent-skills` (read at commit `19d93f9`, 28 Oct 2026, which targets Unity 6.3 LTS / 6000.3). Use it when the collection is not installed. Each entry says what goes wrong and how to confirm it.

### A1. Scripting and lifecycle

- **Pick callbacks by purpose.** `Awake` caches references and runs once on load. `OnEnable` subscribes to events. `Start` does setup that depends on other objects' `Awake`. `Update` is per-frame logic and input polling. `FixedUpdate` is physics. `LateUpdate` is camera follow after movement. `OnDisable` and `OnDestroy` unsubscribe and clean up.
- **`GetComponent` in `Update`** searches every frame. Cache in `Awake`.
- **`public` fields just to show them in the Inspector** let any script mutate them. Use `[SerializeField] private`. A plain class needs `[System.Serializable]` to show in the Inspector.
- **`gameObject.tag == "X"`** allocates. Use `CompareTag("X")`.
- **Start order across objects is undefined.** `Start` runs after every `Awake`, but not in a defined order among themselves. Self-setup in `Awake`, cross-object wiring in `Start`.
- **Coroutines stop when the GameObject is disabled.** Setting only the script's `enabled = false` does not stop them. Restart in `OnEnable` if they must survive toggling.
- **Unity 6 replaced `FindObjectOfType` and `FindObjectsOfType`** with `FindFirstObjectByType`, `FindAnyObjectByType` (faster) and `FindObjectsByType(FindObjectsSortMode.None)`. All are slow, so cache the result.
- **`async` methods outlive their object.** `await` is not tied to the GameObject as a coroutine is. Pass `destroyCancellationToken` to `Awaitable` waits, and never await the same `Awaitable` instance twice because instances are pooled.
- **Moving or renaming assets outside the Editor** must move the `.meta` file too. A new `.meta` means a new GUID and broken references. The collection's `check_unity_project.py` (Python 3.10+, read-only) detects duplicate GUIDs, moved files without `.meta`, and missing script references.

### A2. Input System (package `com.unity.inputsystem` 1.x; 1.20 ships with 6.3 LTS)

- **No input at all:** Active Input Handling (Project Settings, Player) is still `Input Manager (Old)`, or the action or map was never enabled. `Both` is needed while any `Input.GetAxis` code remains.
- **Reuse the project-wide actions asset** (`InputSystem_Actions.inputactions` in new Unity 6 projects, assigned in Project Settings, Input System Package) rather than adding a second one. Read with `InputSystem.actions.FindAction("Move")`.
- **Project-wide actions enable every map at startup,** so gameplay actions can fire while a menu is open. Disable the maps you do not want in `Start`, and switch maps for gameplay versus UI instead of guarding every handler.
- **`FindAction` returns null:** the name or `Map/Action` path is wrong, or you edited a different asset than the one assigned.
- **`InvalidOperationException` about the old input backend:** a script still calls `Input.GetKey` while handling is set to New.
- **Button presses read as 0 with `ReadValue`.** Presses are edge events. Use the `performed` callback or `WasPressedThisFrame()`.
- **`Send Messages` handlers never fire:** the receiver must be on the same GameObject as `PlayerInput`.
- **Unsubscribe in `OnDisable`** (`-=`). Re-subscribing in `OnEnable` without unsubscribing doubles handlers.
- **uGUI menu ignores the gamepad after switching to the new Input System:** the scene still has a `StandaloneInputModule`. Replace it with `InputSystemUIInputModule`. UI Toolkit in Unity 6 reads the project-wide UI actions directly.
- Confirm with Window, Analysis, Input Debugger.

### A3. Physics (3D PhysX)

- **Unity 6 renames:** `Rigidbody.velocity` is now `linearVelocity`, `drag` is `linearDamping`, `angularDrag` is `angularDamping` (`angularVelocity` is unchanged). The old names still compile in 6.3 but are obsolete. `PhysicMaterial` is now `PhysicsMaterial` and is a hard compile error in old code.
- **Forces in `Update`** are frame-rate dependent and jittery. Read input in `Update`, store intent, apply forces or `MovePosition` in `FixedUpdate`.
- **Setting `transform.position` on a dynamic Rigidbody** teleports it and skips collision. Use forces, `linearVelocity` or `MovePosition`. If you must write the transform, call `Physics.SyncTransforms()` once before a same-frame query, never every frame.
- **`OnCollision*` needs a collider on both objects and at least one dynamic (non-kinematic) Rigidbody** with the default Contact Pairs Mode. Kinematic versus kinematic or versus static sends no collision messages.
- **Triggers never fire:** a trigger needs a Rigidbody on at least one of the two colliders, and both colliders enabled. Two static triggers do not report.
- **`CharacterController` does not raise `OnCollisionEnter`.** It reports through `OnControllerColliderHit`. Do not add a Rigidbody to fix this, because the two movement modes are mutually exclusive.
- **Raycasts hit triggers by default** (`Physics.queriesHitTriggers` is true). Pass `QueryTriggerInteraction.Ignore`. A ray also returns false for a collider its origin starts inside.
- **Tunnelling:** raise Collision Detection above Discrete. `Continuous` sweeps against static colliders only. `Continuous Dynamic` also sweeps against other continuous dynamic bodies. `Continuous Speculative` works against everything and is cheaper. For bullets, cast a ray or sphere along the trajectory.
- **Concave `MeshCollider` on a moving body:** concave colliders can only be static or kinematic. Enable Convex, or build a compound collider from primitives. Keep scale uniform.
- **A compound body should have exactly one Rigidbody,** on the root. A child Rigidbody makes that child a separate body.
- **Resting body hangs in mid-air** after you move a static collider by its Transform: call `Rigidbody.WakeUp()`.
- **`Time.timeScale = 0`** stops the simulation and callbacks while raycasts still work.
- **Unity 6.3 also ships a separate low-level 2D physics API** (`UnityEngine.LowLevelPhysics2D`) with its own isolated worlds. It is not the `Rigidbody2D` system.
- Confirm with Window, Analysis, Physics Debugger, and the Layer Collision Matrix (Project Settings, Physics).

### A4. Animator

- **String parameter typos fail silently.** Cache `Animator.StringToHash` ints.
- **Transition feels laggy:** `Has Exit Time` is on. Turn it off for responsive, condition-driven transitions.
- **`SetTrigger` sticks or fires late:** no transition consumed it. `ResetTrigger`, or use a `Bool` for sustained conditions.
- **Character slides or will not move:** Apply Root Motion is on while script also moves the transform. Choose one.
- **`CrossFade` duration is normalised** to the state's length. Use `CrossFadeInFixedTime` for seconds.
- **Upper-body layer overrides the whole body:** set the layer's Blend mode, add an Avatar Mask, and tune the layer weight.
- **IK does nothing:** it applies only inside `OnAnimatorIK`, needs IK Pass enabled on the layer, and needs a Humanoid Avatar.
- During a transition, the "current" state is the one being left. Read `GetNextAnimatorStateInfo` while `IsInTransition`.

### A5. ScriptableObjects

- **Runtime edits persist in the Editor.** Keep mutable runtime state in `[System.NonSerialized]` fields and reset them. In a build, asset edits do not persist across launches.
- **Disabled Domain Reload skips `OnEnable`.** With Enter Play Mode Options on and Reload Domain off, already-loaded assets are not re-created, so reset on `EditorApplication.playModeStateChanged` or from a `[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]` method.
- **Per-object state does not belong on a shared asset.** Two enemies with different current HP need the HP on the MonoBehaviour.
- ScriptableObjects have no `Update`. They are authoring assets, not a save file. Destroy instances made with `CreateInstance` when done.

### A6. 2D tilemaps

- **`RuleTile` is not built in.** Install the 2D Tilemap Extras package (`com.unity.2d.tilemap.extras`, 6.0.x for Unity 6.3).
- **One collider per tile hurts performance and leaves seams.** Add `CompositeCollider2D` with a Static `Rigidbody2D` and set Composite Operation to Merge. `usedByComposite` is obsolete and maps to `CompositeOperation.Merge`. Raise the Extrusion Factor if small gaps remain.
- **`SetTile` and `GetTile` take cell coordinates** (`Vector3Int`). Convert with `WorldToCell` and `CellToWorld`.
- **Bulk edits:** `SetTilesBlock` beats per-cell `SetTile`. Use `RefreshTile(cell)` for a few edits, and reserve `RefreshAllTiles()` for whole-map regeneration.
- **Sorting:** set each `TilemapRenderer`'s sorting layer and order. The Tile Palette's Active Tilemap decides where paint lands.

### A7. NavMesh (AI Navigation 2.0)

- **The old Navigation window's Bake tab and the "Navigation Static" flag are gone.** Add a `NavMeshSurface` component and click Bake. Window, AI, Navigation only edits agent types and areas. Install `com.unity.ai.navigation`.
- **Agent warps to the origin or will not move:** it is not on the baked mesh. Spawn on it (`NavMesh.SamplePosition`) and teleport with `agent.Warp`.
- **New geometry ignored:** use a carving `NavMeshObstacle` or call `surface.BuildNavMesh()`.
- **`NavMeshAgent` plus non-kinematic Rigidbody** jitters. Tick Is Kinematic while the agent is in control. An agent and an obstacle on the same object spin or slide, so enable only one at a time.
- **`SetDestination` every frame** is wasteful for slow targets. Re-path on a timer such as 0.2 seconds.
- **`OffMeshLink` is deprecated.** Use `NavMeshLink` (`Unity.AI.Navigation`). `CalculatePath` returning `PathPartial` means the target is on a different baked island, so bridge it with a link.
- Keep the agent's radius and height consistent with the baked agent type.

### A8. Builds and CI

- **Scene missing in the build:** it is not in the scene list, or the Build Profile you are building has its own list.
- **`MissingMethodException` only in the build:** managed stripping removed reflection-only code. Lower the stripping level or add a `link.xml` preserve entry.
- **IL2CPP fails on a fresh machine:** the platform C++ toolchain is missing.
- **`BuildPipeline.BuildPlayer` returning is not success.** Check `BuildReport.summary.result` and fail the pipeline otherwise.
- **Other-platform build uses the wrong defines:** switch the platform first, or launch with `-buildTarget` in batch mode (`SwitchActiveBuildTarget` is not available there).
- **Addressables content stale:** build it explicitly in CI. The "Build Addressables on Player Build" setting can depend on each machine's Preferences.
- **Do not ship a Development build** (`BuildOptions.Development` enables the profiler and is slower).
- Headless form: `Unity -batchmode -quit -nographics -projectPath <path> -buildTarget win64 -executeMethod BuildScript.BuildWindows -logFile -`. Check the exit code.
- For 6.3 LTS the scripting backend choice is Mono or IL2CPP. The CoreCLR backend seen in the 6.7 beta is experimental and not for production.

### Primary documentation to cite

- Event function execution order: `https://docs.unity3d.com/Manual/execution-order.html`
- Input System package manual: `https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/index.html`
- AI Navigation 2.0 manual: `https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/index.html`
- 2D Tilemap Extras 6.0 manual: `https://docs.unity3d.com/Packages/com.unity.2d.tilemap.extras@6.0/manual/index.html`
- Domain reloading: `https://docs.unity3d.com/Manual/domain-reloading.html`

## Appendix B: Genre playbooks for Unity

How to compose a Unity game for each genre. The skill bindings come from the collection's router and genre skills (`rpg`, `fps-shooter`, `platformer`, `roguelike`, `card-game`, `puzzle`, `survival-crafting`, `tower-defense`, `visual-novel`). The component and data-asset suggestions are standard Unity practice rather than text taken from the genre skills, so check them against the user's project before presenting them as the only way.

### B1. Shared architecture

Ownership rule used across the collection: the engine skill owns API and syntax, the discipline skill owns the portable concept, and the genre skill owns structure and glue. Advise in that order, so the answer does not re-teach a primitive that a Unity skill already covers.

Default Unity structure to recommend unless the project already has its own:

- Content as data: one ScriptableObject per item, card, enemy, tower, recipe or weapon, referenced from MonoBehaviours (`unity-scriptableobjects`).
- Per-instance state (current HP, cooldown, inventory contents) on MonoBehaviours or plain serializable classes, never on the shared asset.
- Decoupling with event-channel ScriptableObjects instead of singletons (`unity-scriptableobjects`, whose own `references/event-channels.md` covers the pattern).
- Persistence separate from authoring assets: a save model that serialises ids and numbers, not scene objects (`save-systems`).
- UI reads state through events, not polling (`game-ui-ux`).

### B2. RPG

Skills: `unity-scriptableobjects` then `rpg`, with `dialogue-systems`, `save-systems`, `game-ui-ux`.

- Item and ability definitions are ScriptableObjects. The inventory is runtime data holding item ids and quantities.
- Stats are numbers with modifiers. Keep base stats and a list of modifiers, and compute the final value on demand, so equipment can be removed cleanly.
- Quests and dialogue are data plus a small state machine. Use Yarn or Ink through `dialogue-systems` for branching text.
- Save the inventory, stats, quest flags and scene id. Version the save from the first release (`save-systems` covers migration).
- Likely pitfalls: mutating a shared ScriptableObject at runtime, and saving object references instead of ids.

### B3. FPS or first-person shooter

Skills: `unity-physics`, `unity-csharp-scripting`, `unity-input-system`, `unity-navmesh`, then `fps-shooter`, `game-ai`, `camera-systems`, `game-feel`.

- The collection has no dedicated 3D essentials skill for Unity (only Godot and Unreal have one), so the router binds the controller to `unity-csharp-scripting` plus `unity-physics`. Say this gap out loud.
- Hitscan weapons use a layer-masked `Physics.Raycast`. Ignore triggers with `QueryTriggerInteraction.Ignore` unless they are hit volumes. Projectiles that move fast need a cast along the trajectory or a Continuous collision mode.
- Choose the controller deliberately: `CharacterController` (simple, no Rigidbody, reports hits through `OnControllerColliderHit`) or a Rigidbody controller (full physics). They are mutually exclusive on one object.
- Enemies: `NavMeshAgent` for movement, a state machine or behaviour tree for decisions (`game-ai`).
- Look and aim input comes from the Input System. Camera shake and recoil belong in `camera-systems` and `game-feel`.

### B4. Platformer (2D)

Skills: `unity-csharp-scripting`, `unity-physics` for concepts, `unity-tilemap-2d`, then `platformer`, `level-design`, `camera-systems`, `game-feel`.

- There is no dedicated Unity 2D movement skill. Note that `unity-physics` documents the 3D `Rigidbody` API, while a 2D platformer normally uses `Rigidbody2D` and `Collider2D`, which have different types. Adapt the concepts and say so.
- The `platformer` skill covers jump feel (coyote time, jump buffering, variable jump height). Apply movement in `FixedUpdate` when it drives a Rigidbody.
- One-way platforms use `PlatformEffector2D` with Use One Way (from the platformer skill).
- Tilemap collision: one merged `CompositeCollider2D` per solid layer (`unity-tilemap-2d`).

### B5. Roguelike

Skills: `procedural-gen`, `unity-tilemap-2d`, then `roguelike`, with `game-ai`, `save-systems`, `game-feel`.

- Generate tile data from a seed, write it with `SetTilesBlock`, and keep the seed in the save so runs are reproducible.
- Items, monsters and drop tables are ScriptableObjects.
- Run state (current floor, inventory, seed) is saved separately from meta-progression.
- Rebuild navigation after generating geometry if agents need it (`surface.BuildNavMesh()` for 3D).

### B6. Card game or deckbuilder

Skills: `unity-scriptableobjects`, `unity-csharp-scripting`, then `card-game`, `game-ui-ux`.

- Each card is a ScriptableObject. Effects run through an interpreter that reads effect data, so new cards need no new code in most cases.
- Keep the rules engine free of UnityEngine types where possible, so it can be unit-tested, and let UI subscribe to its events.
- Random ranges differ between engines (the `card-game` skill notes that Unity's integer `Random.Range` excludes the upper bound), so check bounds when porting rules.

### B7. Puzzle or match-3

Skills: `unity-tilemap-2d` or a plain grid model, then `puzzle`, `level-design`, `game-feel`.

- Model the board as data (a 2D array of ids) and render it separately. The resolution loop (match, clear, fall, refill) is plain C# in `unity-csharp-scripting` style.
- Juice from `game-feel`: easing, squash and stretch, and hit stop make clears satisfying.

### B8. Survival and crafting

Skills: `unity-scriptableobjects`, `save-systems`, `procedural-gen`, then `survival-crafting`, `game-ui-ux`.

- Items and recipes are ScriptableObjects, and the tech tree is data.
- Building and placement uses grid snapping (`unity-tilemap-2d` for 2D, and the Unity grid or snapping for 3D with no dedicated skill).
- Saving a mutable world is the hard part. Save changes to a generated world as deltas against the seed.

### B9. Tower defense

Skills: `game-ai`, `unity-navmesh` or waypoint movement, then `tower-defense`, `level-design`, `game-ui-ux`.

- Enemies follow a path. Use `NavMeshAgent` when the player can alter the route, or waypoints when it is fixed.
- Towers, enemies and waves are ScriptableObjects, so balance changes need no code.
- Targeting rules (first, last, strongest, closest) are small strategy objects.

### B10. Visual novel

Skills: `dialogue-systems`, `save-systems`, `game-ui-ux`, then `visual-novel`.

- Author in Yarn or Ink and drive the UI from the dialogue runner's events.
- Save the story variables and the current node.
- For typewriter text, reveal characters with `TMP_Text.maxVisibleCharacters` (TextMeshPro) instead of growing the string, because re-wrapping every frame makes words jump between lines (from the `visual-novel` skill).

### B11. Prototyping and jams

Skills: `prototype-fast`, `game-jam`.

- Answer one question ("is it fun?") with greybox primitives and a hard timebox, then decide to keep or kill. Do not build save systems or menus before that answer.
- For jams, cut scope first. The `game-jam` skill governs scope and submission.

## Appendix C: Topics the collection does not cover

The collection has eight Unity-specific skills (scripting, input, physics, animation, ScriptableObjects, 2D tilemap, NavMesh, build pipeline). Several Unity concerns are covered only by engine-neutral discipline skills with short Unity notes, and some are not covered at all. This appendix says what to rely on in each case, and how confident to be.

Confidence key: **collection** means the guidance comes from a collection skill that was read. **general** means widely known Unity practice that was not verified against the collection, so tell the user to confirm it against the Unity manual for their exact version.

### C1. Covered only by engine-neutral skills (with Unity notes)

**Performance** (`performance-optimization`, collection)
- Measure first. Unity tools: Profiler (CPU, GPU, Memory, Rendering modules) and Frame Debugger for draw calls. In code, `ProfilerRecorder` on "CPU Main Thread Frame Time" and "GPU Frame Time"; release players need Frame Timing Stats enabled in Player Settings.
- Allocation fixes: cache references, reuse buffers (for example `Physics.RaycastNonAlloc` with a preallocated array), avoid LINQ and boxing in `Update`.
- Batching: share materials and atlas textures. Under URP or HDRP, the SRP Batcher takes precedence over "Enable GPU Instancing" for compatible shaders, so check the Frame Debugger. For many identical meshes, the GPU Resident Drawer needs Forward+ and compute-capable APIs, not OpenGL ES.
- Overdraw comes from stacked transparents, particles and full-screen effects.

**Cameras** (`camera-systems`, collection)
- Cinemachine 3 uses `CinemachineCamera` in namespace `Unity.Cinemachine`, with a `CinemachineBrain` on the real Camera that blends automatically. A third-person orbit uses Orbital Follow plus a Cinemachine Deoccluder to stop wall clipping.
- Shake: `CinemachineBasicMultiChannelPerlin` for continuous noise, or a `CinemachineImpulseSource` on the hitter with a `CinemachineImpulseListener` on the camera for one-off impacts.
- Without Cinemachine, follow with `Vector3.SmoothDamp` in `LateUpdate`.

**UI** (`game-ui-ux`, collection)
- uGUI: anchor RectTransforms to corners and use layout groups. Canvas Scaler set to Scale With Screen Size, reference 1920x1080, Match 0.5 (use 1.0 if the HUD is height-critical). Read `Screen.safeArea` to set anchors for notches. Set a selected object with `EventSystem.SetSelectedGameObject` so a gamepad works, and use `InputSystemUIInputModule` with the Input System package.
- UI Toolkit: scaling lives on the `PanelSettings` asset. Call `Focus()` on the first focusable element.
- Pitfall: a corner-anchored uGUI element grows off-screen if its pivot was left at (0.5, 0.5).

**Audio** (`audio-design`, collection, engine-neutral)
- Route sounds through a few mixer groups, work in decibels, duck music under dialogue, and vary SFX. Unity maps this to the AudioMixer. Specific AudioMixer API details are not in the collection.

**Shaders** (`shader-programming`, collection, engine-neutral)
- GLSL fundamentals with HLSL equivalents. It does not teach Shader Graph or URP shader structure.

**Saving** (`save-systems`, collection, engine-neutral)
- Concepts only: what to serialise, atomic writes, schema versioning, migration. Choose a Unity serializer (`JsonUtility`, or a JSON library) yourself and say which and why.

### C2. Not covered

These have no collection skill. Answer from the Unity manual for the user's version and label the confidence.

- **URP, HDRP and Built-in render pipelines, post-processing, lighting and lightmaps** (general).
- **Shader Graph and custom render features** (general).
- **Addressables beyond the build-pipeline notes** (the collection only notes that content must be built explicitly in CI and that the load path must be checked) (general for the rest).
- **Netcode, multiplayer and Unity Gaming Services** (general).
- **Timeline and cutscenes** (the animation skill names them as out of scope) (general).
- **Particles and VFX Graph** (general).
- **Localization, accessibility** (general).
- **DOTS and ECS** (general).
- **Mobile specifics** such as ads, in-app purchases, safe areas beyond `Screen.safeArea` (general).
- **A dedicated 3D character controller and 2D platformer movement** (the router names these as gaps and binds to `unity-csharp-scripting` plus `unity-physics`).
- **Unit and play-mode testing with the Unity Test Framework** (general).

### C3. Official Unity skills, if present

Some agent setups also have Unity's own official skills installed, named with a `unity:` prefix (for example for UI Toolkit, URP migration, localization, multiplayer services, sprite atlases, TextMeshPro optimisation, IAP and ads). If the agent can see them, prefer them for the gap topics above, and use this skill for overall architecture and for the topics the collection covers. Do not assume they exist. Check the available skills list first.

### C4. How to answer a gap question

1. Say plainly that this topic is outside the Unity skills in the collection.
2. Answer from general Unity practice at the level you are sure of, and avoid exact menu paths, property names or package versions you cannot verify for the user's version.
3. Point to the Unity manual or package manual for the exact version, and tell the user what to check in the Editor to confirm the advice worked.
4. If the user's agent has web access and the question depends on a current version, look the detail up rather than guessing.

## Appendix D: Collection map and provenance

Research notes from reading the repository directly (shallow clone, last commit 28 Oct 2026, `19d93f9`). Licence: Apache-2.0. Source: `https://github.com/gamedev-skills/awesome-gamedev-agent-skills`.

### D1. What it is

A catalogue of game-development skills in the Agent Skills format (`SKILL.md` with YAML frontmatter, optional `references/`, `scripts/`), plus a `router` skill that detects the engine from project files and loads only the matching skills. The skills.sh listing shows 78 entries, which are the 77 authored skills plus the router. Layout: `skills/unity/`, `skills/disciplines/`, `skills/genres/`, `skills/workflows/`, and folders for other engines.

### D2. Skills relevant to Unity work

**Unity-specific (8), target Unity 6.3 LTS (6000.3):**

| Skill | Lines (SKILL.md) | Extras |
|---|---|---|
| `unity-csharp-scripting` | 159 | `references/lifecycle-and-coroutines.md`; `scripts/check_unity_project.py` (915 lines, read-only `.meta` and GUID checker) |
| `unity-input-system` | 180 | `references/rebinding.md` |
| `unity-physics` | 189 | `references/raycasting-and-joints.md` |
| `unity-animation` | 131 | `references/blend-trees-and-ik.md` |
| `unity-scriptableobjects` | 143 | `references/event-channels.md` |
| `unity-build-pipeline` | 169 | `references/ci-build-script.md` |
| `unity-tilemap-2d` | 131 | none |
| `unity-navmesh` | 165 | none |

**Engine-neutral disciplines with Unity notes (use alongside the above):** `game-feel`, `game-ui-ux`, `level-design`, `performance-optimization`, `audio-design`, `game-ai`, `ai-behavior-trees-utility-ai`, `camera-systems`, `save-systems`, `input-systems`, `procedural-gen`, `physics-tuning`, `shader-programming`, `dialogue-systems`, `create-game-assets`. Each is roughly 140 to 210 lines. `physics-tuning` has the most Unity mentions (13), `game-ui-ux` has 9.

**Genre playbooks:** `rpg`, `roguelike`, `fps-shooter`, `card-game`, `puzzle`, `platformer`, `survival-crafting`, `tower-defense`, `visual-novel`. They compose engine and discipline skills and bind to Unity skills by name.

**Workflows:** `prototype-fast`, `game-jam`, `steam-publish`, `itch-publish`. These are engine-independent.

**Router:** `router` (266 lines plus `references/routing-table.md`, `engine-detection.md`, `custom-engines.md`). Detects Unity by `Assets/` together with `ProjectSettings/ProjectVersion.txt`.

### D3. Excluded skills

Godot (16 skills), Unreal (6), Roblox (8), Phaser (2), three.js (3), PixiJS (1), Bevy, pygame, LÖVE, Ebitengine and Defold. They are not relevant to Unity advice.

### D4. Quality assessment

Strengths found:

- Every Unity skill pins a stated engine version (6.3 LTS) and uses Unity 6 API names, including the `linearVelocity` rename, `PhysicsMaterial`, `FindFirstObjectByType`, AI Navigation 2.0 and `NavMeshLink` replacing `OffMeshLink`.
- Pitfall lists are specific and verifiable (for example the Contact Pairs Mode rule for kinematic collisions, the disabled Domain Reload effect on ScriptableObject resets, `Continuous` sweeping static colliders only).
- A consistent structure: when to use, when not to use, core workflow, patterns with code, pitfalls, references, related skills. The "when not to use" sections route cleanly between skills.
- Primary-source links (Unity manual and package manual) are cited.
- A version-support policy (`docs/VERSION-SUPPORT.md`, checked 24 Oct 2026): Unity baseline is 6.3 LTS (6000.3.27f1 at last check), existing projects keep their own version, and engine majors are never mixed.
- The repository has a validator script and tests, which suggests the skills are maintained as a set.

Weaknesses and gaps:

- Only eight Unity skills. No dedicated skill for uGUI or UI Toolkit, Cinemachine, URP or Shader Graph, Addressables (build notes only), Netcode, Timeline, a 3D character controller or 2D platformer movement. The router acknowledges the movement and 3D gaps.
- `unity-physics` is 3D PhysX only. The 2D physics API is mentioned as out of scope, so 2D games must adapt it.
- The Unity-specific skills target a single LTS (6.3). Projects on 2022 LTS or earlier will hit differences, because several APIs were renamed in Unity 6.
- The engine-neutral skills carry only short Unity notes, so Unity-specific depth for audio, shaders and saving is thin.
- Install counts on skills.sh (7.1K to 7.7K for the Unity skills, 12.3K for `game-feel`) show uptake but say nothing about correctness.

Overlap: `unity-input-system` and `input-systems`, `unity-physics` and `physics-tuning`, `unity-navmesh` and `game-ai`, and `unity-tilemap-2d`, `level-design` and `procedural-gen` are deliberate pairs. The engine skill owns API and syntax, and the discipline owns the portable concept.

### D5. Install and compatibility

- `npx skills add gamedev-skills/awesome-gamedev-agent-skills` installs the router and all skills for the detected agent. Flags: `--list` to preview, `-g` for every project, `-a <agent>` to target a tool such as `claude-code`. Needs Node.js 22.20 or later.
- Claude Code plugin route: `claude plugin marketplace add gamedev-skills/awesome-gamedev-agent-skills`, then `claude plugin install router@awesome-gamedev-agent-skills` and `claude plugin install unity@awesome-gamedev-agent-skills`.
- The format is the open Agent Skills standard, so the same files load in Claude Code, Cursor, Windsurf, Cline, Codex, Gemini CLI, GitHub Copilot and others without conversion.

### D6. Provenance and how this skill relates

The appendices in this skill paraphrase and condense the collection's guidance so the advisor still works without it. The collection is the authoritative source: when it is installed, read the matching skill and prefer it over the condensed copy, and re-check the condensed notes whenever Unity ships a new LTS. The collection's own policy is a quarterly review, so treat this skill's notes as dated 28 Oct 2026.