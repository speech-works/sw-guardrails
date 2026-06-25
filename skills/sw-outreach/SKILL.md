---
name: sw-outreach
description: >-
  Draft or review outbound messages from Speechworks to the stuttering
  community — replies and cold intros to people who stutter (PWS), self-help
  groups (TISA and peer orgs), SLPs and clinicians, NGOs and funders, and pilot
  or partner contacts. Use when writing a WhatsApp/email/DM reply, a cold
  outreach, a pitch follow-up, or pilot-tester recruitment, or when asked to make
  a message sound less AI or salesy, more honest, and grounded in what the
  product can actually back. Pairs with the sw-guardrails review skill.
---

# Speechworks outbound messaging

A writer and reviewer for the messages Speechworks sends *out* — to people who
stutter, the self-help groups and SLPs who work beside them, and the NGOs and
partners who might help. The job of almost every one of these messages is
narrow: **earn the next step** (a reply, a call, a coffee, a pilot seat), not
win the whole argument in text.

Two failure modes kill these messages. **Sounding AI or salesy** makes a careful
reader stop trusting you. **Over-claiming** — implying a cure, a clinical
validation, or a feature that isn't built — gets you caught by exactly the
clinicians and advocates whose trust you need. This skill exists to avoid both:
sound like a real founder, and say only what the product and the research
actually support.

It assumes the therapeutic-integrity rules in the companion **sw-guardrails**
skill (no fluency-as-goal, no cure claims, no shame framing). Run every draft
through that skill too — outbound copy is a Speechworks artifact like any other.

## When to use

Trigger on: "draft a reply to [community contact / SHG / SLP / NGO]," "write a
cold intro to…," "follow up on the pitch," "recruit pilot testers," "make this
message sound less AI / less salesy / more grounded," "is this honest about what
we've actually built?", or before sending anything outbound to the stuttering
community.

## How to draft (or review) a message

1. **Pin the single goal.** Name the one next step this message should produce,
   and make it the smallest viable ask. One message, one ask.
2. **Identify the audience** and calibrate (§D). A PWS individual, an SHG, an
   SLP, and a funder need different leads and different depth.
3. **Ground every claim** in the product and research before you write it (§B).
   If you can't back it, don't claim it.
4. **Draft point-wise.** If they asked questions, mirror their structure so they
   can scan answers against questions. Lead with real context, not a pitch.
5. **Apply the voice rules** (§C) and the honesty calibration (§B).
6. **Run sw-guardrails** over the draft (cure / fluency / shame / person-first).
7. **Walk the pre-send checklist** (§E). Fix anything that depends on something
   outside the message (a link, a build, a person's consent to be named).

---

## A. Goal & structure

### A1 — One message, one ask 🟡
Most outbound messages have exactly one job. Don't bury it under three asks or a
feature tour. End on the smallest next step that moves things forward.
- ❌ "Let me know if you want a demo, or the deck, or to invest, or to introduce
  me to your group, or…"
- ✅ "Would this weekend work for a coffee?"

### A2 — Mirror their questions 🔵
When someone asks specific questions, answer them in their order, point-wise.
It reads as respect and makes the message scannable. Don't fold five questions
into one paragraph of prose.

### A3 — Lead with real context, not a pitch 🟡
Open with something true and human (why you're building this, how you found
them), then get to the substance. Never invent or inflate the backstory — use
the founder's actual story. A manufactured "we" or a fake origin reads false and
is hard to walk back.

### A4 — Close with the next step, once 🔵
A single clear, low-friction ask. Offer to come to them. Make saying yes easy.

---

## B. Grounding & honesty (the part that earns trust)

### B1 — Verify every product claim before you write it 🔴
Before asserting any feature, metric, integration, or research basis, confirm it
exists in the product (the Speechworks frontend `sw-fe-m-2` and backend `sw-be-2`
repos) or with the team. Treat this like asking the CTO. If you can't show it,
don't claim it — downgrade to what's true ("we're working toward…",
"we're exploring…").
- ❌ Asserting a metric, framework mapping, or integration nobody has checked.
- ✅ "We track [X], grounded in [the actual mechanism]" — verified first.

### B2 — Keep the honest limits in 🟡
Stated limits build trust with careful evaluators; softening them reads as spin.
Keep lines like these, don't dress them up:
- "No published case studies yet."
- "It isn't clinically validated — our grounding is the research and ongoing
  input from clinicians and the community."
- "Pricing isn't locked yet."

### B3 — Don't claim more than the product/research supports 🔴
Calibrate to what's real, not what's aspirational. In particular:
- **Fluency:** Speechworks does not score fluency. Say that plainly; don't
  imply fluency gains or a "smoother voice" outcome.
- **The science:** the measurement model is grounded in an established, validated
  framework for the *lived experience* of stuttering, not a scale we invented.
  Frame it as that. Do **not** claim formal mappings or certifications the code
  doesn't carry (e.g. an explicit standards-framework mapping) — if pressed,
  name the actual assessment basis and offer to go deeper in person.
- **No phantom features:** never reference a capability that isn't shipped
  (e.g. a crisis-support integration, region-specific resources) unless it's
  actually wired and relevant to the recipient's region.

### B4 — Cite people and institutions with a verifiable link, and with consent 🟡
Naming an SLP, clinic, institution, or advocate is powerful, but only with a
link the recipient can check, and only if that person/org is comfortable being
cited to an outside contact. An unverifiable name-drop is worse than none.
- ✅ "shaped by input from clinicians, including [Institution] (link) and experts
  like [Name] (link)."
- ❌ A list of impressive names with no links and no one's say-so.

### B5 — Hold the deep detail for the conversation 🔵
Lead with philosophy and a live demo; keep heavy clinical or technical depth
(the exact assessment instrument, the estimation math, citations) in reserve for
the meeting, where you can defend it. Translate it to plain English in the
message instead.
- ❌ "We use mathematical state estimation against a standards framework across
  five metrics."
- ✅ "We track how someone's relationship with speaking is changing over time,
  with a model careful enough not to treat one bad day as a setback."

---

## C. Voice (don't sound AI, don't sound salesy)

### C1 — No throat-clearing honesty phrases 🟡
They signal the opposite of what they claim. Cut "to be honest," "honestly,"
"I'll be straight with you," "I won't lie," "let me be real." Just say the honest
thing.

### C2 — No AI cadence / negative parallelism 🟡
Avoid the templated rhythm: "it isn't X, it's Y," "not a replacement, but a
companion," "this isn't about fluency, it's about confidence." One natural
contrast in a message is fine; a stack of them is a tell.
- ❌ "Strictly a companion, never a replacement."
- ✅ "It sits alongside what an SHG or therapist already does."

### C3 — No rule-of-three triads for rhythm 🔵
Three-item lists used for cadence ("the support, the experience, and the
direction") read as generated. Use the list the content actually needs.

### C4 — Go easy on em-dashes; no hype words 🔵
Prefer periods, commas, parentheses. Ban inflated adjectives: "revolutionary,"
"cutting-edge," "seamless," "game-changing," "world-class," "magical,"
"supercharge."

### C5 — Plain, specific, human 🔵
Concrete lived detail beats abstraction (this is also sw-guardrails B2). Short
punchy sentences are fine and read as a person, not a model.

> Read the finished draft aloud once. If a sentence sounds like a brochure or a
> chatbot, rewrite it the way you'd actually say it to this person.

---

## D. Audience calibration

| Audience | Lead with | Can go deeper on | Watch out for |
|---|---|---|---|
| **PWS (individual)** | peer / lived-experience; the practice between sessions; person-first language | how it respects their experience and choices | any cure/fluency framing, pity or inspiration-porn, pressure |
| **SHG / TISA & peer orgs** | companion-not-replacement; genuine interest in their perspective and help | the acceptance-aligned philosophy; the consent-based buddy model | sounding like you'll replace them; selling; over-claiming validation |
| **SLP / clinician** | the model is grounded; honest validation status | the actual assessment basis; how progress is estimated; cite sources | implying clinical validation you don't have |
| **NGO / funder / partner** | the gap you're closing; reach and affordability | subsidy plans; low per-user cost (on-device work); intended impact | hype; vague or invented impact numbers |
| **Investor** | (defer to the GFS / pitch notes) | traction *honestly* | inflating traction or readiness |

Across all audiences, the therapeutic-integrity rules hold: stuttering is
approached, not cured or suppressed; success is lived-experience change, not
fluency; people who stutter are the protagonists.

---

## E. Pre-send checklist

- [ ] **One clear ask**, and it's the smallest viable next step.
- [ ] **Every product/feature/metric claim is verified** in the code or with the
  team, or clearly framed as intent (§B1, B3).
- [ ] **Honest limits kept in**, not softened (§B2).
- [ ] **Every named person/org has a working link** and is OK being cited (§B4).
- [ ] **Anything the message points at actually works** — the site renders on
  mobile (and the anchor resolves), the build is installable by an outsider, the
  asset opens.
- [ ] **Ran sw-guardrails** — no cure, no fluency-as-goal, no shame, person-first.
- [ ] **Read aloud for AI tells** — no "honestly," no triads, at most one "not X"
  contrast, few em-dashes, no hype words.
- [ ] **Both spellings** (stutter / stammer) where the copy is public or
  SEO-facing (less critical in a 1:1 DM).

---

## Quick reference — phrases to catch and cut

```
# Throat-clearing honesty (C1)
to be honest|honestly,|i'?ll be straight|i (won'?t|will not) lie|let me be real

# AI cadence / negative parallelism (C2)
it'?s not (just )?\w+,? it'?s|isn'?t about \w+,? (it'?s|but)|never a replacement|not (a|just) \w+, but

# Hype / inflated (C4)
revolutionary|cutting.?edge|seamless|game.?chang|world.?class|magical|supercharge|unlock your

# Over-claim (B3) — verify or cut
clinically (proven|validated)|\bcure\b|guarantee|100% ?fluen|smoother voice|proven results

# Fluency-as-outcome (B3 / sw-guardrails A2)
fluency (score|gain|improv)|stutter.?free|reduce(d)? stutter|speak fluently
```

Grep is a first pass. Judgement wins: one honest "it isn't validated yet" is the
point, not a violation; a stack of "not X, but Y" is the tell.

---

## A worked line (before → after)

Reframing the differentiator, from a draft that over-claimed and sounded
generated to one that's honest and human:

- ❌ "Our algorithm de-prioritises fluency and ranks it last, tracking progress
  against the WHO framework across five metrics using mathematical state
  estimation."
- ✅ "Most tools measure fluency as a count, which we think is the least useful
  number you can hand a person who stutters. We don't score fluency at all. We
  track the speaker's overall experience of stuttering, across five sides of real
  communication, with a model careful enough not to treat one bad day as a
  setback."

The second version claims only what's true, drops the jargon (saved for the
meeting), and reads like a person.

---

## Related

- **sw-guardrails** (`../sw-guardrails/SKILL.md`) — the therapeutic-integrity and
  brand-voice reviewer. Always run drafts through it; this skill assumes its
  rules.
- The Speechworks positioning and voice notes (team docs) hold the fuller
  audience-mindset write-up and the current product facts to verify claims
  against.

## Disclaimer

This skill captures communication and outreach guidance for Speechworks. It is
not clinical advice and not a substitute for assessment or therapy by a qualified
speech-language pathologist.
