# Strudel CC — Genre Presets & Performance Techniques
# Ready-to-run blueprints and live coding strategies

---

## GENRE BLUEPRINT PRESETS

### TECHNO (134 BPM, A minor)
```javascript
setcpm(134 / 4)

const drums = stack(
  s("bd").euclid(4, 8).gain(1),
  s("~ sd").gain(.9),
  s("hh*8").degradeBy(.15).gain(.6),
  s("oh").euclid(2, 8).gain(.5)
).bank("RolandTR909")

const bass = note("<a1 [a1 c2] e1 [g1 a1]>").s("sawtooth")
  .lpf(sine.range(200, 1200).slow(8))
  .attack(.005).release(.2).gain(.9)

const lead = n("<0 [2 4] <3 5> [~ <4 1>]>").scale("A4:minor")
  .s("sawtooth").jux(rev)
  .lpf(1800).hpf(200)
  .room(.3).delay(.125)
  .gain(.6).slow(2)

stack(drums, bass, lead)
```

### HOUSE (128 BPM, C minor)
```javascript
setcpm(128 / 4)

const drums = stack(
  s("bd*4").gain(1),
  s("~ cp").gain(.85),
  s("hh*8").swing(2).gain(.5),
  s("oh").euclid(3, 8).gain(.45)
).bank("RolandTR909")

const bass = note("<c2 [c2 eb2] f1 [g1 c2]>").s("gm_synth_bass_1")
  .lpf(800).attack(.01).release(.3).gain(.85)

const lead = chord("<Cm7 Fm7 Gm7 Eb7>/2").voicing()
  .s("gm_electric_piano_1")
  .room(.5).gain(.55)

stack(drums, bass, lead)
```

### AFROBEATS (110 BPM, F minor)
```javascript
setcpm(110 / 4)

const drums = stack(
  s("bd").euclid(3, 8).gain(1),
  s("sd").euclid(2, 8).gain(.8),
  s("hh*4 [hh hh]*2").swing(4).gain(.55),
  s("perc").euclid(5, 16).gain(.5)
)

const bass = note("<f2 [f2 ab2] c2 [eb2 f2]>").s("gm_electric_bass_finger")
  .attack(.01).release(.25).lpf(600).gain(.9)

const lead = n("<0 2 [4 5] [3 ~]>").scale("F:minor")
  .s("gm_electric_guitar_clean")
  .room(.35).delay(.25).gain(.6)

stack(drums, bass, lead)
```

### AMBIENT (85 BPM, D dorian)
```javascript
setcpm(85 / 4)

const drums = stack(
  s("bd").euclid(2, 8).gain(.5),
  s("hh*4").degradeBy(.4).gain(.2)
)

const bass = note("<d2 [d2 e2] a2 [g2 a2]>").s("sine")
  .attack(.2).release(1.5).gain(.7).slow(2)

const texture = n("<0 2 4 [6 7]>").scale("D4:dorian")
  .s("gm_pad_2_warm")
  .jux(rev).room(.9).size(4)
  .attack(1).release(2).slow(2).gain(.5)

stack(drums, bass, texture)
```

### DRILL (140 BPM, G minor)
```javascript
setcpm(140 / 4)

const drums = stack(
  s("bd").struct("x ~ ~ x ~ ~ x ~").gain(1),
  s("sd").euclid(2, 16).slow(2).gain(.9),
  s("hh*16").degradeBy(.3).gain(.45),
  s("oh").euclid(3, 16).gain(.4)
)

const bass = note("<g1 [g1 bb1] d2 [c2 g1]>").s("sawtooth")
  .lpf(400).attack(.005).decay(.1).sustain(.5).release(.1)
  .gain(.95)

const lead = n("<0 [2 4] 5 [3 ~]>").scale("G4:minor")
  .s("triangle").jux(rev)
  .room(.4).gain(.6).slow(2)

stack(drums, bass, lead)
```

### JAZZ (95 BPM, C minor)
```javascript
setcpm(95 / 4)

const drums = stack(
  s("bd").euclid(3, 8).gain(.8),
  s("~ [rim, sd:<2 3>]").room(.2).gain(.75),
  s("hh*8").swing(2).gain(.45),
  s("oh").euclid(2, 8).gain(.35)
)

const bass = note("<c2 [c2 eb2] f2 [g2 bb2]>").s("gm_acoustic_bass")
  .room(.3).gain(.85)

const lead = chord("<Cm7 Fm9 Gm7 Eb7>/2").voicing()
  .s("gm_electric_piano_1")
  .room(.5).sometimes(x => x.room(.9)).gain(.55)

stack(drums, bass, lead)
```

---

## LIVE PERFORMANCE TECHNIQUES

### Energy Escalation (gradually build up intensity)
```javascript
// Layer 1: Just drums
stack(drums)

// Layer 2: Add bass
stack(drums, bass)

// Layer 3: Full arrangement
stack(drums, bass, lead)

// Layer 4: Mutate — double the drum speed every 4 cycles
stack(
  drums.every(4, fast(2)),
  bass,
  lead.jux(rev)
)
```

### Filter Automation (classic DJ transition)
```javascript
// Open filter over 8 cycles — brings in a layer
const filtered = bass.lpf(sine.range(100, 2000).slow(8))
```

### Rhythmic Displacement
```javascript
// Offset bass by 1/8th note for syncopation
bass.late(1/8)

// Offset lead by half a cycle for call-response feel
lead.early(.5)
```

### Texture Variation Patterns
```javascript
// Random drop-out: ~30% of beats silent
s("hh*16").degradeBy(.3)

// Conditional mutation every 8 cycles
lead.every(8, x => x.rev().room(.9))

// Chunk-based variation: apply reverb to one quarter each cycle
bass.chunk(4, x => x.room(.8))

// Occasional pitch jump
lead.rarely(x => x.add(note(12)))
```

### Polyrhythmic Layering
```javascript
// 5 over 8 (clave-style)
s("bd").euclid(5, 8)

// 7 over 16 (Afro-Cuban)
s("cp").euclid(7, 16)

// Layered polyrhythm
stack(
  s("bd").euclid(4, 16),
  s("cp").euclid(7, 16),
  s("hh").euclid(3, 16)
)
```

### Spatial Movement
```javascript
// Left=original, right=reversed
lead.jux(rev)

// Partial jux with 50% blend
lead.juxBy(.5, rev)

// Slow pan sweep
lead.pan(sine.slow(4))

// Random stereo scatter
s("hh*8").pan(rand)
```

### Sidechain / Ducking Effect
```javascript
// Duck other sounds when kick hits — orbit-based approach
s("bd*4").orbit(1)
// Other patterns on orbit 2 will duck with .duck() in supported versions
```

---

## STRUDEL REPL KEYBOARD SHORTCUTS

```
Ctrl/Cmd + Enter    Execute all code
Ctrl/Cmd + .        Stop all sound
Ctrl/Cmd + /        Comment/uncomment line
Alt + Enter         Execute block only (under cursor)
```

## LABELED STATEMENT PATTERN (REPL multi-block style)

```javascript
// Each $: block runs independently
$: s("bd*4,hh*8").bank("RolandTR909")

$: note("<c2 eb2 f2 g2>").s("sawtooth").lpf(600)

_$: s("cp sd").gain(.5)   // underscore = muted
```

---

## COMMON GOTCHAS & FIXES

| ❌ Problem | ✅ Fix |
|-----------|--------|
| `s("bass")` — no sound | Use `s("sawtooth")` or `s("gm_acoustic_bass")` |
| `note("c3")` — no pitch | OK for melody; but pair with `.s("sine")` etc. |
| Silence after changing code | Re-run with Ctrl+Enter |
| Continuous LFO not working | Add `.segment(16)` to discretize the signal |
| `delayfeedback(.95)` getting loud | Keep feedback < 1.0 |
| Two patterns fighting over reverb | Use `.orbit(2)` and `.orbit(3)` to separate |
| `fast()` duplicating sounds | Use `.fastGap()` to speed without repeating |
| Scale notes out of range | Add octave number to scale: `"C4:minor"` |
| Random sounds inconsistent | Use `ribbon()` to loop a deterministic seed |

---

## INSPIRATIONAL EXAMPLES (from strudel.cc showcase)

### Groove with chord voicing (iReal style):
```javascript
samples('github:eddyflux/crate')
setcps(.75)
let chords = chord("<Bbm9 Fm9>/4").dict('ireal')
stack(
  stack(
    s("bd").struct("<[x*<1 2> [~@3 x]] x>"),
    s("~ [rim, sd:<2 3>]").room("<0 .2>"),
    n("[0 <1 3>]*<2!3 4>").s("hh"),
  ).bank('crate'),
  chords.offset(-1).voicing().s("gm_epiano1:1").phaser(4).room(.5),
  n("<0!3 1*2>").set(chords).mode("root:g2").voicing().s("gm_acoustic_bass"),
)
```

### Generative melody with perlin:
```javascript
setcpm(85/4)
n(perlin.segment(8).range(0, 7))
  .scale("D4:minor")
  .s("gm_pad_2_warm")
  .room(.8).gain(.6).slow(2)
```

### Euclidean percussion stack:
```javascript
setcpm(134/4)
stack(
  s("bd").euclid(4, 8),
  s("sd").euclid(3, 8).late(.5),
  s("hh").euclid(7, 16).gain(.5),
  s("oh").euclid(2, 16).gain(.4),
  s("cp").euclid(1, 8).late(.25)
).bank("RolandTR909")
```
