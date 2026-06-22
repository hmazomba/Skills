# Strudel CC — Sounds, Scales & Drum Machines Reference
# Source: https://strudel.cc/learn/samples + https://strudel.cc/workshop/first-notes/

---

## BUILT-IN SAMPLE SOUNDS (always available, no loading needed)

### Drum Sounds (use with `s("...")`)
```
bd        kick drum
sd        snare drum
hh        hi-hat (closed)
oh        open hi-hat
cp        clap
rim       rimshot
lt        low tom
mt        mid tom
ht        high tom
rd        ride cymbal
cr        crash cymbal
perc      percussion
```

### Melodic/Tonal Samples
```
piano     acoustic piano
casio     casio keyboard
```

### Synthesizer Oscillator Types (use with `.s("...")`)
```
sawtooth  saw wave (bright, rich harmonics — good for bass/lead)
square    square wave (hollow, buzzy)
sine      pure sine (clean sub bass, very smooth)
triangle  triangle wave (mellow, warm)
supersaw  detuned multi-saw (fat, wide)
pulse     pulse wave (thinner than square)
```

---

## GENERAL MIDI SOUND FONTS (always available)

Use with `.s("gm_soundname")`. Access variations with `.n(0–127)`:

### GM Drums & Rhythm
```
gm_woodblock  gm_agogo  gm_taiko_drum  gm_synth_drum
```

### GM Strings
```
gm_violin      gm_viola        gm_cello         gm_contrabass
gm_tremolo_strings  gm_pizzicato_strings  gm_orchestral_harp
gm_string_ensemble_1  gm_string_ensemble_2
gm_synth_strings_1    gm_synth_strings_2
```

### GM Guitar
```
gm_acoustic_guitar_nylon  gm_acoustic_guitar_steel
gm_electric_guitar_jazz   gm_electric_guitar_clean
gm_electric_guitar_muted  gm_overdriven_guitar
gm_distortion_guitar      gm_guitar_harmonics
```

### GM Bass
```
gm_acoustic_bass          gm_electric_bass_finger
gm_electric_bass_pick     gm_fretless_bass
gm_slap_bass_1            gm_slap_bass_2
gm_synth_bass_1           gm_synth_bass_2
```

### GM Keys & Pads
```
gm_acoustic_grand_piano  gm_bright_acoustic_piano
gm_electric_grand_piano  gm_honkytonk_piano
gm_electric_piano_1      gm_electric_piano_2  gm_epiano1
gm_harpsichord  gm_clavinet
gm_pad_1_new_age   gm_pad_2_warm     gm_pad_3_polysynth
gm_pad_4_choir     gm_pad_5_bowed    gm_pad_6_metallic
gm_pad_7_halo      gm_pad_8_sweep
```

### GM Brass & Winds
```
gm_trumpet    gm_trombone  gm_tuba   gm_muted_trumpet
gm_french_horn  gm_brass_section  gm_synth_brass_1  gm_synth_brass_2
gm_soprano_sax  gm_alto_sax  gm_tenor_sax  gm_baritone_sax
gm_oboe  gm_english_horn  gm_bassoon  gm_clarinet
gm_flute  gm_recorder  gm_pan_flute  gm_blown_bottle
```

### GM Mallets & World
```
gm_celesta  gm_glockenspiel  gm_music_box  gm_vibraphone
gm_marimba  gm_xylophone     gm_tubular_bells  gm_dulcimer
gm_sitar    gm_banjo         gm_shamisen       gm_koto
gm_kalimba  gm_bag_pipe      gm_fiddle         gm_shanai
```

### GM Synth Leads
```
gm_lead_1_square   gm_lead_2_sawtooth  gm_lead_3_calliope
gm_lead_4_chiff    gm_lead_5_charang   gm_lead_6_voice
gm_lead_7_fifths   gm_lead_8_bass_lead
```

---

## DRUM MACHINES (use with `.bank("Name")`)

Access via `s("bd sd hh oh cp rim rd cr").bank("RolandTR909")`.
The bank name is prepended automatically: `RolandTR909_bd`, etc.

```
RolandTR808     // classic hip-hop kick, long decay
RolandTR909     // house/techno kick, snare, hats
RolandTR707     // 80s pop/electronic
RolandTR606     // vintage electronic
AkaiLinn        // 80s digital drum machine
LinnDrum        // classic pop/funk
AlesisHR16      // 90s rave
ViscoSpaceDrum  // electronic space sounds
EMT                            
```

To see sample counts: open the **Sounds** tab in the REPL → **Drum Machines**.
Each machine lists available sounds + counts, e.g. `RolandTR909_hh(4)`.

Select variants: `s("hh").bank("RolandTR909").n("<0 1 2 3>")`

---

## SCALES

Use with `n("0 1 2 3").scale("Root:type")` or `.scale("C4:minor")` (with octave).

### Common Scales
```
C:major          C:minor          C:dorian         C:phrygian
C:lydian         C:mixolydian     C:locrian
C:minor:pentatonic  C:major:pentatonic
C:harmonic:minor    C:melodic:minor  
C:blues          C:chromatic
```

### Modal Scales
```
C:dorian         // minor-ish but with raised 6th — great for groove/funk
C:phrygian       // Spanish/flamenco flavour
C:lydian         // bright, dreamlike (raised 4th)
C:mixolydian     // blues rock feel (dominant 7th)
C:locrian        // dissonant, dark
```

### Exotic
```
C:whole:tone     C:diminished
C:enigmatic      C:neapolitan:major  C:neapolitan:minor
C:persian        C:arabian           C:hungarian:minor
C:byzantine
```

### Scale by Genre Default
```
Techno → A:minor          (dark, industrial)
Afrobeats → F:minor       (warm, grooving)
Ambient → D:dorian        (open, meditative)
Jazz → C:minor            (versatile, urban)
Drill → G:minor           (menacing)
House → C:minor           (emotional, euphoric)
Afrobeats alt → G:mixolydian  (bright groove)
Afrobeats alt → Bb:major      (joyful)
```

---

## CHORD VOICINGS

```javascript
chord("<Cm7 Fm7 Gm7>")           // basic chord pattern
chord("<Cm9 Fm9>/4")              // slow chord changes (every 4 cycles)
chord("...").dict('ireal')        // use iReal Pro chord dictionary
chord("...").voicing()            // auto voice lead
chord("...").offset(-1).voicing() // voice lead one octave down
chord("...").anchor("D5")         // constrain to anchor pitch range
chord("...").n("0 2 1 3").voicing() // arpeggiate through chord voices
```

**Common chord symbols:** `C Cm Cmaj7 Cm7 C7 Cdim Caug Csus4 Cm9 Cmaj9 C6 Cm6 C9`

---

## SYNTHESIS NOTES

### Synth voice selection by genre:
```
Sub bass      → .s("sine")       // clean sub, no harmonics
Dark bass     → .s("sawtooth")   // rich harmonics, filter well
Digital bass  → .s("square")     // hollow, punchy
Warm bass     → .s("triangle")   // mellow, acoustic-adjacent
Lead synth    → .s("supersaw")   // fat, wide, pad-like
Pluck synth   → .s("sawtooth").decay(.1).sustain(0)
```

### Loading custom wavetables (e.g. Bubo waveforms):
```javascript
samples('github:bubobubobubobubo/dough-waveforms')
note("c2").s("wt_dbass")  // digital bass wavetable
note("c4").s("wt_flute")  // flute wavetable
```
