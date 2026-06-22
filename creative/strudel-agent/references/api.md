# Strudel CC — Verified API Reference
# Source: https://strudel.cc (docs scraped June 2026)

---

## CONSTRUCTORS (Pattern Factories)

```javascript
s("bd sd hh")                   // sample playback — triggers named sounds
note("c4 e4 g4")                // melodic notes using MIDI notation
n("0 2 4").scale("C:minor")     // scale-degree binding (preferred for melodic layers)
chord("<Cm7 Fm7>")              // chord voicings
freq("440 550 660")             // raw frequency in Hz
```

## PATTERN COMBINATORS

```javascript
stack(a, b, c)     // layer simultaneously (all play at once)
cat(a, b, c)       // concatenate: each gets one full cycle (= "<a b c>")
seq(a, b, c)       // sequence: all crammed into one cycle (= "a b c")
arrange(
  [4, patA],       // play patA for 4 cycles
  [2, patB]        // then patB for 2 cycles
)
```

Chaining versions:
```javascript
s("hh*4").stack(note("c4(5,8)"))
s("hh*4").cat(note("c4(5,8)"))
```

---

## TIME MODIFIERS

```javascript
.slow(n)           // stretch pattern over n cycles (= /n in mini notation)
.fast(n)           // speed up pattern by n (= *n in mini notation)
.rev()             // reverse events within each cycle
.iter(n)           // shift start point each cycle (rotates through n versions)
.iterBack(n)       // like iter but in reverse direction
.palindrome()      // alternates forward/backward every cycle
.early(t)          // nudge pattern earlier by t cycles (micro-timing)
.late(t)           // nudge pattern later by t cycles
.compress(a, b)    // compress into the timespan [a, b], leaving gaps
.zoom(a, b)        // plays only the portion from a to b of the pattern
.linger(f)         // select fraction f of pattern, loop to fill cycle
.ply(n)            // repeat each event n times within its slot
.segment(n)        // sample pattern n times per cycle (discretize signals)
.clip(f)           // multiply note duration by f; cuts sample at end
.swing(n)          // apply swing feel (shorthand: swingBy(1/3, n))
.swingBy(x, n)     // manual swing: delay 2nd half of each n-th slice by x
.ribbon(offset, cycles)  // loop a specific slice of the timeline
.fastGap(n)        // fast but leaves gap (doesn't repeat to fill)
.euclid(hits, steps)            // Euclidean rhythm distribution
.euclidRot(hits, steps, rot)    // Euclidean with rotation offset
.euclidLegato(hits, steps)      // Euclidean held until next hit
```

---

## CONDITIONAL & STRUCTURAL MODIFIERS

```javascript
.every(n, fn)         // apply fn every n cycles
.firstOf(n, fn)       // apply fn on 1st cycle of every n
.lastOf(n, fn)        // apply fn on last cycle of every n
.chunk(n, fn)         // divide into n parts, apply fn to each in turn
.chunkBack(n, fn)     // like chunk but in reverse order
.when(pat, fn)        // apply fn when binary pattern is 1
.struct(pat)          // impose rhythmic structure from binary pattern
.mask(pat)            // silence when pat is 0
.hush()               // silence this pattern
.off(t, fn)           // layer a transformed copy offset by t cycles
.jux(fn)              // split: left channel normal, right channel gets fn
.juxBy(amt, fn)       // partial jux: blend by amount 0–1
.layer(fn1, fn2)      // layer multiple transformed copies
.pick(n, [...])       // select from list by index pattern
```

---

## RANDOM MODIFIERS

```javascript
.sometimes(fn)            // apply fn ~50% of events
.often(fn)                // apply fn ~75% of events
.rarely(fn)               // apply fn ~25% of events
.almostAlways(fn)         // apply fn ~90% of events
.almostNever(fn)          // apply fn ~10% of events
.sometimesBy(p, fn)       // apply fn with probability p (0–1)
.someCycles(fn)           // apply fn to ~50% of cycles
.someCyclesBy(p, fn)      // apply fn to cycles with probability p
.degrade()                // randomly remove ~50% of events
.degradeBy(p)             // randomly remove p fraction of events
choose(a, b, c)           // pick one randomly each event
chooseCycles(a, b, c)     // pick one randomly each cycle (= randcat)
irand(n)                  // random integer 0 to n-1 (use with n())
rand                      // continuous random 0–1 (use with .range())
perlin                    // smooth random (Perlin noise) 0–1
brand                     // binary random: 0 or 1
```

---

## AUDIO EFFECTS (Signal Chain Order)

```
[source] → gain (ADSR) → lpf → hpf → bpf → vowel → coarse → crush → shape 
         → distort → tremolo → compressor → pan → phaser → [split: dry / delay / reverb]
```

### Volume & Gain
```javascript
.gain(0–1)              // amplitude 0=silent, 1=full
.velocity(0–1)          // alias for gain
.pan(-1–1)              // stereo position (0=center, -1=left, 1=right)
.postgain(n)            // gain after all effects
.orbit(n)               // send to orbit/channel n (separate reverb/delay)
```

### ADSR Amplitude Envelope
```javascript
.attack(s)              // time to peak in seconds (alias: .att())
.decay(s)               // time to sustain level (alias: .dec())
.sustain(0–1)           // sustain level (alias: .sus())
.release(s)             // fade-out time after note end (alias: .rel())
.adsr("a:d:s:r")        // combined: .adsr(".01:.1:.8:.2")
```

### Filters
```javascript
.lpf(hz)                // lowpass filter cutoff (alias: cutoff, ctf, lp)
.lpq(0–50)              // lowpass resonance (alias: resonance)
.hpf(hz)                // highpass filter cutoff (alias: hp, hcutoff)
.hpq(0–50)              // highpass resonance (alias: hresonance)
.bpf(hz)                // bandpass filter center frequency (alias: bp, bandf)
.bpq(n)                 // bandpass resonance (alias: bandq)
.vowel("a e i o u")     // formant vowel filter
.ftype("12db"|"ladder"|"24db")  // filter character
```

### Filter Envelopes
```javascript
.lpa(s)   .lpd(s)   .lps(0–1)   .lpr(s)   .lpenv(depth)  // lowpass envelope
.hpa(s)   .hpd(s)   .hps(0–1)   .hpr(s)   .hpenv(depth)  // highpass envelope
.bpa(s)   .bpd(s)   .bps(0–1)   .bpr(s)   .bpenv(depth)  // bandpass envelope
```

### Reverb
```javascript
.room(0–1)              // reverb send amount
.roomsize(n)            // reverb size (recalculates IR — use sparingly)
.size(n)                // alias for roomsize
.ir("sample")           // use a sample as impulse response
```

### Delay
```javascript
.delay(0–1)             // delay send amount
.delaytime(t)           // delay time in cycles
.delayfeedback(0–1)     // delay feedback (⚠️ never >= 1)
// Mini-notation shorthand: .delay(".5:.125:.8") = amount:time:feedback
```

### Distortion & Saturation
```javascript
.distort(n)             // distortion amount
.shape(n)               // waveshape distortion (softer)
.crush(n)               // bit crusher
.coarse(n)              // sample rate reduction
```

### Spatial & Modulation
```javascript
.phaser(n)              // phaser effect amount
.phasercenter(hz)       // phaser center frequency
.phasersweep(hz)        // phaser LFO sweep range
.tremolo(n)             // tremolo (tremolosync alias)
.tremolosync(cycles)    // sync tremolo to cycle rate
.tremolodepth(d)        // tremolo depth
```

### Pitch & Playback
```javascript
.speed(n)               // sample playback speed (2=octave up, .5=octave down)
.begin(0–1)             // sample start point
.end(0–1)               // sample end point
.unit("c"|"s")          // c=cycles, s=seconds for begin/end
.n(n)                   // select sample variant (e.g. hh:0, hh:1...)
.note(n)                // set pitch (MIDI note or name)
.freq(hz)               // set frequency directly
.detune(cents)          // pitch detune in cents
.bank("RolandTR909")    // prepend drum machine name to samples
```

### FM Synthesis
```javascript
.fm(n)                  // FM ratio (frequency modulation)
.fmh(n)                 // FM harmonic
.fmenv(depth)           // FM envelope depth
```

### Chord & Voicing (Advanced)
```javascript
.voicing()              // voice lead chords smoothly
.anchor("D5")           // constrain voicing around anchor pitch
.mode("root:c2")        // set chord root note
.set(chords)            // bind n() to a chord pattern
.arp("0 1 2")           // arpeggiate stack notes by index
.offset(n)              // shift chord voicing by n octaves
```

---

## CONTINUOUS SIGNALS (use with .range() for modulation)

```javascript
sine          // 0–1 sine wave (one per cycle)
cosine        // 0–1 cosine wave
saw           // 0–1 sawtooth wave  
tri           // 0–1 triangle wave
square        // 0–1 square wave
rand          // 0–1 smooth random
perlin        // 0–1 Perlin noise (smooth)
irand(n)      // integer 0 to n-1
brand         // binary 0 or 1
mouseX        // mouse X position 0–1
mouseY        // mouse Y position 0–1

// Bipolar versions (-1 to 1):
sine2  cosine2  saw2  tri2  square2  rand2
```

**Using signals as modulation:**
```javascript
.lpf(sine.range(200, 2000).slow(4))     // filter LFO over 4 cycles
.gain(perlin.range(0.6, 0.9))           // organic volume variation
.pan(sine2.slow(8))                      // slow stereo pan
.cutoff(rand.range(500, 8000))           // random cutoff per event
```

**⚠️ Continuous LFO caveat:** Signals are only sampled when a sound event fires.
To fake a continuous LFO, discretize with `.segment(n)`:
```javascript
s("supersaw").segment(16).lpf(tri.range(100, 5000).slow(2))
```

---

## VALUE OPERATORS

```javascript
.add("n")         // add n to all values
.sub("n")         // subtract n from all values  
.mul("n")         // multiply all values by n
.div("n")         // divide all values by n
.round()          // round to nearest integer
.range(min, max)  // scale 0–1 signal to min–max range
.rangex(min, max) // exponential range scaling (useful for frequency)

// Example: shift scale degrees up by 7 every 4 cycles
n("0 1 2 3").scale("C:minor").every(4, x => x.add(7))
```

---

## TEMPO

```javascript
setcpm(BPM / 4)   // set tempo (cycles per minute = BPM / beats-per-cycle)
setcps(n)         // set cycles per second (setcps(0.5) = 120 BPM at 4/4)
.cpm(90)          // set tempo inline on pattern (chained)
```

**Common BPM → setcpm conversions:**
```
120 BPM = setcpm(30)    // House
128 BPM = setcpm(32)    // Tech House
134 BPM = setcpm(33.5)  // Techno
140 BPM = setcpm(35)    // Drill/DNB
85 BPM  = setcpm(21.25) // Ambient
110 BPM = setcpm(27.5)  // Afrobeats
```

---

## MINI-NOTATION CHEATSHEET

```
~           rest (silence)
x           sound event  
[a b]       subdivide: a and b share one beat
<a b>       alternate: a on cycle 1, b on cycle 2
a,b         polyrhythm / simultaneous (same as stack in mini)
a*n         repeat a n times
a/n         slow a down by n (plays every n cycles)
a!n         replicate a n times (same as a a a...)
a@n         weighted duration (a takes n times longer)
a?          50% chance of playing (degradeBy 0.5)
a?0.3       30% chance of playing (degradeBy 0.7)
a:n         select sample variant n (e.g. "hh:2")
{a b c}%n   polyrhythm: fit a b c into n steps
0..7        numeric range shorthand (= "0 1 2 3 4 5 6 7")
```

---

## LOADING CUSTOM SAMPLES

```javascript
samples('github:username/reponame')    // load from GitHub repo
samples('bubo:waveforms')              // load from Bubo CDN
samples({ kick: ['kick.wav', 'kick2.wav'] }, 'https://mysite.com/samples/')
```
