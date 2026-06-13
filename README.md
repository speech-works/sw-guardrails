# sw-guardrails

> 🚧 **Under active development.** Guidelines, severities, and grep patterns will
> change as we learn. Pin a commit if you depend on exact behaviour.

A [Claude Code](https://docs.claude.com/en/docs/claude-code) **skill** — and a
living checklist — that reviews any [Speechworks](https://speechworks.app)
artifact against the therapeutic-integrity and brand guidelines that govern how
we talk about stuttering and stammering.

It checks **words and code alike**: blog posts, marketing and landing copy, UI
strings, AI Coach / LLM prompts, analytics event names, metric and KPI names,
dashboard tiles, schema fields, and the copy embedded in source files.

---

## Why this exists

Speechworks builds practice tools for people who stutter (and the
speech-language pathologists who work beside them). The risk in that work is
subtle: **a product or a sentence that worships fluency actively harms the
people it's meant to help.**

This is not an opinion — it's the unanimous, decades-old position of the
clinicians who built the field, most of whom stuttered themselves. The guiding
ideas:

- **Stuttering is an iceberg.** What a listener sees — blocks, repetitions,
  word-swaps — is the tip. The mass below the waterline is shame, fear, guilt,
  avoidance, isolation, and a fantasy of being cured. That mass is what keeps
  people stuck.
  <br>— Joseph G. Sheehan, ch. 6, and Larry Molt, ch. 21 [[1]](#references)
- **Trying *not* to stutter deepens the disorder.** The way out is *through*:
  acceptance, reduced avoidance, self-disclosure, and learning to stutter more
  easily — not less.
  <br>— Peter Ramig, ch. 9; Gerald Moses, ch. 15 [[1]](#references)
- **There is no cure; the goal is a changed relationship with stuttering.**
  <br>— Charles Van Riper, ch. 28; Margaret Neely, ch. 12 [[1]](#references)
- **Success is approach, not fluency** — situations entered, disclosures made,
  avoidance dropped, risks taken. David Daly literally counted *attempts* by
  moving paperclips from one pocket to the other.
  <br>— Walter Manning, ch. 22; David Daly, ch. 16 [[1]](#references)

So the load-bearing rule of this skill — its **"fluency god" guardrail** — is:
never imply a cure, and never make fluency the headline metric. Let fluency be a
side effect; measure and celebrate approach instead.

A fuller write-up of the audience mindset and how it maps to product and content
decisions lives in the Speechworks team notes; this repo is the enforceable
distillation.

---

## What it checks

The full, authoritative ruleset is in [`SKILL.md`](./SKILL.md). Summary:

| Section | Focus | Example 🔴 catch |
| --- | --- | --- |
| **A. Therapeutic integrity** | cure claims, fluency-as-metric, avoidance/suppression framing, shame, relapse, honest tone | "Become 100% fluent" · a `fluencyScore` KPI · "take a deep breath and the words will come" |
| **B. Voice & framing** | peer authority, lived detail, Coach-as-companion (not judge), dual PWS/SLP audience | a faceless-AI "we'll fix you" tone |
| **C. Language** | both *stuttering* + *stammering*, person-first in brand voice, no pity/othering | "sufferer", "afflicted", "victim" |
| **D. Code** | metric/event/var names, dashboards, LLM prompts, embedded copy, schema enums | event `stutter_detected` · toast "Great — no stutters detected!" |

Findings are reported with a severity — 🔴 **block** / 🟡 **warn** / 🔵 **note** —
a reason, and a concrete rewrite.

---

## Install & use

This repo is laid out so it drops straight into a project's skills directory.

```bash
# from your project root
git clone https://github.com/speech-works/sw-guardrails.git \
  .claude/skills/sw-guardrails
```

That yields `.claude/skills/sw-guardrails/SKILL.md`, which Claude Code discovers
automatically. Then, in a Claude Code session:

```
/sw-guardrails review web/src/app/page.tsx
/sw-guardrails is this landing copy on-message?
/sw-guardrails audit our analytics event names
```

To keep it updated: `git -C .claude/skills/sw-guardrails pull` (or add it as a
git submodule).

You can also use [`SKILL.md`](./SKILL.md) as a **plain checklist** in PR reviews
or editorial sign-off, independent of Claude Code — the grep quick-reference at
the bottom is a fast first pass for any CI step.

---

## Status & roadmap

- [x] Core guidelines (A–D), severities, grep quick-reference
- [ ] Worked before/after examples for each rule
- [ ] A CI-friendly grep/lint script (`scripts/check.sh`)
- [ ] Test fixtures (known-good and known-bad samples) to guard against drift
- [ ] Tighten person-first vs reclaimed-"stutterer" detection
- [ ] Versioned releases / changelog once the ruleset stabilises

Issues and PRs welcome — especially from people who stutter and from SLPs. If a
rule here ever contradicts lived experience, the lived experience wins; open an
issue.

---

## References

The guidelines synthesise (and quote briefly, with attribution) the following
sources. Quotations are short and used for commentary; all rights remain with
the original publishers.

1. **Hood, S. B. (Ed.). (2008). _Advice to Those Who Stutter_ (2nd ed.,
   Publication No. 0009). Stuttering Foundation of America. ISBN 0‑933388‑39‑X.**
   28 first-person chapters by speech-language pathologists who stutter
   themselves. PDF:
   <https://www.stutteringhelp.org/sites/default/files/Migrate/book0009_may2010.pdf>
   Chapters drawn on directly:
   - Ch. 1 — Lon L. Emerick, *Express Yourself or Go by Freight* (admit the need
     to change; drop the "excess baggage")
   - Ch. 2 — Dorvan H. Breitenfeldt, *Managing Your Stuttering…* (advertising /
     acknowledging you stutter; eye contact)
   - Ch. 3 — Margaret Rainey, *Stuttering: What You Can Do About It* ("you are
     your own worst critic")
   - Ch. 4 — Hugo H. Gregory, *Two Sides of the Coin* (ERA‑SM; stutter‑more‑fluently)
   - Ch. 6 — Joseph G. Sheehan, *Message to a Stutterer* (the **iceberg**; "you
     can stutter your way out of this problem")
   - Ch. 7 — Frederick P. Murray, *Toward Freer Speech* ("you have the choice of
     *how* you stutter")
   - Ch. 8 — James L. Aten, *Overcoming Fear and Tension* (positive planning vs.
     anticipated failure)
   - Ch. 9 — Peter R. Ramig, *Don't Ever Give Up!* ("the most disabling aspect…
     results from our attempts not to stutter")
   - Ch. 10 — J. David Williams, *Basic Goals for a Person Who Stutters*
   - Ch. 12 — Margaret M. Neely, *Suggestions for Self‑Therapy* (nothing "cures";
     one can *manage*)
   - Ch. 13 — Henry Freund, *Self‑Improvement After Unsuccessful Treatments*
     (relapse is expected; a trusted companion)
   - Ch. 14 — Harold L. Luper, *Some Helpful Attitudes…* (realistic goals;
     establish→transfer→maintain)
   - Ch. 15 — Gerald R. Moses, *Message to Adult Stutterers* (reduce avoidances;
     judge by *approach*)
   - Ch. 16 — David A. Daly, *…Gaining and Sustaining Improved Fluency* (count
     attempts; the honest, non‑promising clinician)
   - Ch. 17 — Joseph G. Agnello, *Change: Potential Qualities Become Actualities*
     (fake‑stutter / the diner story; reactive→proactive)
   - Ch. 18 — Richard M. Boehmler, *Four Steps to Freedom* (identify, plan, work,
     maintain)
   - Ch. 19 — Bill Murphy, *Recovery Journal* (shame stories; normalizing)
   - Ch. 20 — Sol Adler, *Face Your Fears*
   - Ch. 21 — Larry Molt, *Attacking the Iceberg…* (forgiveness, understanding,
     courage, patience; the "pimple" analogy — the flaw is bigger to you than to
     anyone else)
   - Ch. 22 — Walter H. Manning, *Finding Your Own Path Without Professional
     Help* ("things I do *because* I stutter"; "don't chase the fluency god")
   - Ch. 23 — Paul E. Czuchna, *Guidelines* (covert vs. overt stutterer)
   - Ch. 24 — Robert W. Quesal, *Knowledge, Understanding, and Acceptance*
   - Ch. 25 — Gary J. Rentschler, *Maintaining Dignity While Living With
     Stuttering* (the listener "explanation"; the wheelchair analogy)
   - Ch. 26 — Kenneth O. St. Louis, *Your Life Is Too Important to Spend It
     Worrying About Stuttering*
   - Ch. 27 — Harold B. Starbuck, *Do‑It‑Yourself Kit for Stutterers* ("the kit
     was empty — you already have the tools")
   - Ch. 28 — Charles Van Riper, *Putting It Together* ("there are no magical
     cures… you can change your abnormal reactions")
2. **Stuttering Foundation of America** — myths/facts, brochures, and clinician
   referral resources. <https://www.stutteringhelp.org>
3. **The Stuttering Homepage** (Judy Kuster, ed.) — links, essays, and self-help
   resources. <https://www.mnsu.edu/comdis/kuster/stutter.html>

The requirement to carry **both spellings** ("stuttering" + "stammering") is a
Speechworks SEO/audience decision (UK/India search behaviour), not from the book
above — see the Speechworks team's SEO notes.

---

## Disclaimer

This skill encodes communication and brand guidance distilled from the sources
above. **It is not clinical advice and is not a substitute for assessment or
therapy by a qualified speech-language pathologist.** Any misrepresentation of
the cited work is the maintainers' alone.

## License

[MIT](./LICENSE) © Speech Works.
