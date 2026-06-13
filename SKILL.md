---
name: sw-guardrails
description: >-
  Review any Speechworks artifact — blog posts, marketing/landing copy, UI
  strings, AI Coach prompts, analytics event names, metric/KPI names, dashboard
  tiles, or code — against Speechworks' therapeutic-integrity and brand
  guidelines for stuttering/stammering content. Use when asked to check, review,
  audit, or lint content or code for adherence to the guidelines, brand voice,
  the "fluency god" guardrail, or whether copy is on-message for people who
  stutter and the SLPs who work beside them.
---

# Speechworks content & code guardrails

A reviewer for everything Speechworks ships — words and code alike. It enforces
the **therapeutic integrity** and **brand voice** that make Speechworks help
people who stutter/stammer instead of quietly harming them.

These guidelines are grounded in the Stuttering Foundation book *Advice to Those
Who Stutter* (28 SLPs who stutter themselves) and Speechworks' own positioning
(AI practice for "the 167 hours between sessions": Academy, Dashboard, AI Coach,
plus the lived-experience + evidence blog). The single load-bearing idea: **the
visible stutter is the tip of an iceberg; shame, fear, and avoidance below the
waterline are what keep people stuck. Trying *not* to stutter deepens the
disorder.** Anything that worships fluency works against the user.

## When to use

Trigger on requests like: "check this post / copy / PR against our guidelines,"
"is this on-brand?", "review the AI Coach prompt," "audit our metrics," "does
this respect people who stutter?", or before publishing any user-facing string
or shipping any code that names, scores, or rewards speech.

## How to run a review

1. **Identify the artifact type** — prose (blog/marketing/UI/email), AI Coach or
   LLM prompt, or code (component, schema, analytics event, metric/KPI, var/func
   name, copy embedded in code).
2. **Read it fully**, then scan against every guideline below. For code, also
   `grep` the red-flag patterns in the Quick reference.
3. **Report findings** in the output format below — location, the rule it
   breaks, *why* it matters, a concrete rewrite, and a severity.
4. **Offer to apply fixes** to the working tree (don't edit silently unless the
   user asked for `--fix`-style behavior).
5. If the artifact is clean, say so plainly and note anything borderline.

Severity levels:
- 🔴 **block** — actively harmful or off-mission (cure claims, fluency-as-KPI,
  shaming language). Must change before shipping.
- 🟡 **warn** — undermines voice/integrity or risks misreading. Should change.
- 🔵 **note** — stylistic / SEO / consistency nudge. Nice to fix.

---

## A. Therapeutic integrity (the non-negotiables)

### A1 — Never imply a cure or a miracle 🔴
There is no cure; the goal is a changed *relationship* with stuttering. Banned:
"cure," "fix your stutter," "eliminate stuttering," "stop stuttering forever,"
"overcome it for good," "guaranteed fluency," "speak perfectly," "miracle,"
"breakthrough that ends." This is also what separates Speechworks from the
"quacks" the field warns against.
- ❌ "The proven way to cure your stutter." / "Become 100% fluent."
- ✅ "Practice changing your relationship with stuttering." / "Speak on your terms."

### A2 — Do not make fluency the success metric 🔴
Measuring/celebrating fluency reinforces the perfectionism and shame that keep
people stuck. Success = **approach, disclosure, avoidance reduced, risks taken,
eye contact, situations entered.** Fluency may be a side effect, never the
headline number.
- ❌ A dashboard tile "Stutter-free streak: 6 days," a `fluencyScore`, an event
  `fluency_improved`, "you stuttered 0 times today!"
- ✅ "Feared calls made: 4," "Times you disclosed," "Words you didn't swap,"
  `approachScore`, event `feared_situation_entered`.

### A3 — Frame stuttering as something to approach, not avoid or suppress 🔴
Don't recommend the folk "remedies" every author debunks: "take a deep breath
first," "slow down," "think before you speak," "relax," "just push through,"
"don't stutter." These increase self-consciousness and avoidance.
- ❌ "Take a deep breath and the words will come."
- ✅ "Move forward through the block — stutter easier, not less." / "Stutter on
  purpose to drain the fear."

### A4 — No shame, no defect framing 🟡→🔴
Never position stuttering as a flaw, weakness, embarrassment to hide, or
something "wrong" with the person. Honor it as part of who they are.
- ❌ "Don't let your embarrassing stutter hold you back." / "Hide it better."
- ✅ "Your stuttering is part of you, like your eye colour — it doesn't define
  you."

### A5 — Normalize relapse 🟡
Treat setbacks as expected and non-verdictive; design for re-entry, not punitive
streaks. Maintenance is lifelong and low-dose.
- ❌ "Don't break your streak!" / "Relapse means starting over."
- ✅ "Setbacks are part of the path — here's your re-entry plan."

### A6 — Honest, non-promising tone 🟡
Invitation and partnership, never guarantees. The model: a clinician saying "I
don't know how fluent you'll become — let's work together and see."
- ❌ "In 30 days you'll never block again."
- ✅ "We'll find out what's possible for you, together."

---

## B. Voice & framing

### B1 — Peer authority + lived experience 🟡
The brand's power is "from people who've been through it." Foreground that people
who stutter and the SLPs beside them are behind Speechworks; never a faceless AI
or a detached expert lecturing down.

### B2 — Concrete lived detail over abstraction 🔵
The strongest existing copy is specific ("people who rehearse ordering coffee,"
"people who avoid saying their own name"). Prefer the avoidance-mindset detail
to generic uplift.

### B3 — The AI Coach is a companion, not a judge 🟡
Frame it as the trusted companion / "portable laboratory" for the 167 hours
between sessions — the one who walks into the feared situation with you. Not a
scorer of failures. Adversarial-pressure features must pair each rep with a "win
= you stayed in it" debrief that disproves the catastrophe.

### B4 — Audience is dual 🔵
Both people who stutter (PWS) and speech-language pathologists (SLPs). Don't
write copy that speaks only to one when the surface serves both.

---

## C. Language & terminology

### C1 — Carry both spellings 🔵
Always use BOTH "stuttering" (US) and "stammering" (UK/India — the dominant
search term for this audience) in SEO-facing copy. (See the seo-keyword-strategy
memory.)

### C2 — Respectful, non-pathologizing person reference 🟡
"person who stutters" / "people who stutter (PWS)" is safe and preferred. The
book uses "stutterer" freely and reclaims it; that's fine *inside* first-person
lived-experience writing, but default to person-first in Speechworks' own voice
and marketing. Never "sufferer," "afflicted," "victim," "disabled by," or
"broken."

### C3 — No othering or pity 🟡
Don't frame PWS as objects of sympathy or inspiration-porn. They're the
protagonists, not cautionary tales.

### C4 — Plain, honest claims; cite when clinical 🔵
Lived-experience-meets-evidence. When asserting clinical fact, ground it (the
blog's whole positioning). Avoid hype adjectives ("revolutionary," "magical").

---

## D. Code-specific checks

Apply A1–A2 to code as strictly as to copy — names ship as product.

- **Metric / KPI / variable / function names:** flag `fluency*`, `stutterFree*`,
  `*Score` tied to fluency, `errorCount`, `mistakes`, `failures` for speech.
  Prefer `approachScore`, `situationsEntered`, `disclosures`, `avoidanceDelta`.
- **Analytics / event names:** flag `fluency_improved`, `stutter_detected`,
  `clean_run`. Prefer `feared_situation_entered`, `voluntary_stutter_practiced`,
  `disclosure_rehearsed`.
- **Dashboard tiles / progress UI:** flag any chart trending fluency or
  stutter-count as the hero metric (A2).
- **AI Coach / LLM system prompts:** the coach must not be instructed to score
  fluency, "correct" stutters, reward stutter-free runs, or simulate cruelty
  without a reframing debrief. It should reward approach, disclosure, and staying
  in the situation. Check both the prompt and any rubric/grading schema.
- **Copy embedded in code** (button labels, toasts, empty states, errors): run
  through sections A–C. A toast "Great — no stutters detected!" is a 🔴.
- **Schema field names / enums** (e.g. Sanity post tags, content types): tags
  like `cure`, `fluency-hacks` are 🟡; prefer `acceptance`, `disclosure`,
  `voluntary-stuttering`, `avoidance`, `lived-experience`.

---

## E. Output format

Report as a findings table, most severe first:

| # | Severity | Location | Issue | Why it matters | Suggested fix |
|---|----------|----------|-------|----------------|---------------|

Then a one-line verdict: **ship / fix-then-ship / do-not-ship**, and offer to
apply the fixes. If nothing fires, say "Clean against guardrails" and list any
🔵 notes.

---

## Quick reference — red-flag patterns to grep

```
# Cure / miracle (A1) — almost always 🔴
cure|miracle|breakthrough|guaranteed|forever|100% ?fluen|perfect(ly)? fluent|eliminate stutter|stop stuttering|overcome.*for good
# (tie "100%" to fluency — bare "100%" matches CSS widths and is noise)

# Fluency-as-metric (A2) — 🔴 in code & dashboards
fluency.?score|stutter.?free|clean.?run|fluency_improved|stutter.?detected|no stutters|0 stutters|streak

# Folk remedies (A3) — 🟡/🔴
take a (deep )?breath|slow down|think before you speak|just relax|push through|don'?t stutter

# Shame / defect / pity (A4, C2, C3)
embarrass|ashamed|hide (it|your)|flaw|defect|broken|suffer(er|ing)|afflicted|victim|disabled by

# Missing twin spelling (C1) — note if only one present
stutter (without nearby) stammer   # check both appear in SEO copy
```

Grep is a first pass only — judgement (especially distinguishing reclaimed
first-person "stutterer" from marketing voice) always wins over a keyword hit.
