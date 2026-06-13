# sw-guardrails

> **Status: under active development.** The guidelines, severities, and grep
> patterns will keep changing as we learn. Tagged releases for version pinning
> are on the roadmap; until then, pin a specific commit if you need stable
> behaviour.

A [Claude Code](https://docs.claude.com/en/docs/claude-code) skill, installable
as a plugin or used as a standalone checklist, for reviewing any
[Speechworks](https://speechworks.app) artifact against the therapeutic-integrity
and brand guidelines that govern how we write about stuttering and stammering.

It checks words and code alike: blog posts, marketing and landing copy, UI
strings, AI Coach and other LLM prompts, analytics event names, metric and KPI
names, dashboard tiles, schema fields, and the copy buried inside source files.

---

## Why this exists

Speechworks builds practice tools for people who stutter, and for the
speech-language pathologists who work beside them. The risk in that work is easy
to miss: a product, or a single sentence, that treats fluency as the goal can
quietly harm the people it is meant to help.

This is a long-standing consensus among the clinicians who built the field, most
of whom stuttered themselves:

- Stuttering works like an iceberg. The blocks and word-swaps a listener notices
  are the tip; the larger mass below the surface is shame, fear, guilt,
  avoidance, isolation, and the wish to be cured. That mass is what keeps people
  stuck. (Sheehan, ch. 6; Molt, ch. 21.)
- Trying not to stutter usually makes it worse. The way out runs through it:
  accepting it, avoiding less, telling people, and learning to stutter more
  easily rather than less. (Ramig, ch. 9; Moses, ch. 15.)
- There is no cure. The goal is a changed relationship with stuttering.
  (Van Riper, ch. 28; Neely, ch. 12.)
- Success means approach, not fluency: situations entered, disclosures made,
  avoidance dropped, risks taken. David Daly counted his attempts by moving
  paperclips from one pocket to the other. (Manning, ch. 22; Daly, ch. 16.)

So the rule everything else hangs on, the "fluency god" guardrail, is simple:
never imply a cure, and never make fluency the headline metric. Let fluency be a
side effect, and measure approach instead.

A fuller write-up of the audience mindset, and how it maps to product and
content decisions, lives in the Speechworks team notes. This repo is the
enforceable version.

---

## What it checks

The full ruleset lives in [`SKILL.md`](./SKILL.md). In summary:

| Section | Focus | Example catch |
| --- | --- | --- |
| A. Therapeutic integrity | cure claims, fluency-as-metric, avoidance or suppression framing, shame, relapse, honest tone | "Become 100% fluent"; a `fluencyScore` KPI; "take a deep breath and the words will come" |
| B. Voice and framing | peer authority, lived detail, the Coach as a companion rather than a judge, the dual PWS/SLP audience | a faceless-AI "we'll fix you" tone |
| C. Language | both *stuttering* and *stammering*; person-first in brand voice; no pity or othering | "sufferer", "afflicted", "victim" |
| D. Code | metric, event, and variable names; dashboards; LLM prompts; embedded copy; schema enums | event `stutter_detected`; toast "Great, no stutters detected!" |

Each finding comes with a severity (🔴 block, 🟡 warn, 🔵 note), a reason, and a
concrete rewrite.

---

## Install and use

### As a Claude Code plugin (recommended)

This repo is also a plugin marketplace. Add it once, then install the plugin:

```
/plugin marketplace add speech-works/sw-guardrails
/plugin install sw-guardrails@speechworks
```

To auto-enable it for everyone working in a given repo, commit this to that
repo's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "speechworks": {
      "source": { "source": "github", "repo": "speech-works/sw-guardrails" }
    }
  },
  "enabledPlugins": ["sw-guardrails@speechworks"]
}
```

When a teammate clones that repo and trusts it, Claude Code registers the
marketplace and enables the plugin automatically. Updates come with
`/plugin marketplace update speechworks`.

### As a project skill (no plugin)

Or drop it straight into a project's skills directory:

```bash
# from your project root
git clone https://github.com/speech-works/sw-guardrails.git \
  .claude/skills/sw-guardrails
```

That gives you `.claude/skills/sw-guardrails/SKILL.md`, which Claude Code picks
up automatically. Update it later with `git -C .claude/skills/sw-guardrails pull`,
or pin to a fixed commit instead of tracking `main`:

```bash
git -C .claude/skills/sw-guardrails checkout <commit-sha>
```

### Either way

In a session:

```
/sw-guardrails review web/src/app/page.tsx
/sw-guardrails is this landing copy on-message?
/sw-guardrails audit our analytics event names
```

You can also read [`SKILL.md`](./SKILL.md) as a plain checklist for PR reviews or
editorial sign-off, with no Claude Code involved. The grep quick-reference at the
bottom makes a fast first pass for a CI step.

---

## Status and roadmap

- [x] Core guidelines (A to D), severities, and the grep quick-reference
- [x] Packaged as a Claude Code plugin and marketplace
- [ ] Worked before-and-after examples for each rule
- [ ] A CI-friendly grep script (`scripts/check.sh`)
- [ ] Test fixtures (known-good and known-bad samples) to catch drift
- [ ] Better detection of person-first wording versus the reclaimed word "stutterer"
- [ ] Tagged releases and a changelog once the rules settle

Issues and pull requests are welcome, especially from people who stutter and
from SLPs. If a rule here ever contradicts lived experience, the lived
experience wins, so please open an issue.

---

## References

These guidelines draw on the sources below and quote them briefly, with
attribution. Quotations are short and used for commentary; all rights stay with
the original publishers.

1. **Hood, S. B. (Ed.). (2008). _Advice to Those Who Stutter_ (2nd ed.,
   Publication No. 0009). Stuttering Foundation of America. ISBN 0-933388-39-X.**
   Twenty-eight first-person chapters by speech-language pathologists who stutter
   themselves. PDF:
   <https://www.stutteringhelp.org/sites/default/files/Migrate/book0009_may2010.pdf>.
   Chapters drawn on directly:
   - Ch. 1: Lon L. Emerick, *Express Yourself or Go by Freight* (admit the need
     to change; drop the "excess baggage").
   - Ch. 2: Dorvan H. Breitenfeldt, *Managing Your Stuttering…* (advertising, or
     acknowledging that you stutter; eye contact).
   - Ch. 3: Margaret Rainey, *Stuttering: What You Can Do About It* (you are your
     own worst critic).
   - Ch. 4: Hugo H. Gregory, *Two Sides of the Coin* (ERA-SM; the
     stutter-more-fluently approach).
   - Ch. 6: Joseph G. Sheehan, *Message to a Stutterer* (the iceberg; "you can
     stutter your way out of this problem").
   - Ch. 7: Frederick P. Murray, *Toward Freer Speech* (you have a choice about
     *how* you stutter).
   - Ch. 8: James L. Aten, *Overcoming Fear and Tension* (positive planning
     instead of anticipated failure).
   - Ch. 9: Peter R. Ramig, *Don't Ever Give Up!* (the most disabling part comes
     from our attempts not to stutter).
   - Ch. 10: J. David Williams, *Basic Goals for a Person Who Stutters*.
   - Ch. 12: Margaret M. Neely, *Suggestions for Self-Therapy* (nothing cures it;
     you can manage it).
   - Ch. 13: Henry Freund, *Self-Improvement After Unsuccessful Treatments*
     (relapse is expected; a trusted companion helps).
   - Ch. 14: Harold L. Luper, *Some Helpful Attitudes…* (realistic goals;
     establish, transfer, then maintain).
   - Ch. 15: Gerald R. Moses, *Message to Adult Stutterers* (reduce avoidances;
     judge yourself by whether you approached the situation).
   - Ch. 16: David A. Daly, *…Gaining and Sustaining Improved Fluency* (count
     attempts; the honest clinician who promised nothing).
   - Ch. 17: Joseph G. Agnello, *Change: Potential Qualities Become Actualities*
     (fake stuttering and the diner story; moving from reactive to proactive).
   - Ch. 18: Richard M. Boehmler, *Four Steps to Freedom* (identify, plan, work,
     maintain).
   - Ch. 19: Bill Murphy, *Recovery Journal* (shame stories; normalizing).
   - Ch. 20: Sol Adler, *Face Your Fears*.
   - Ch. 21: Larry Molt, *Attacking the Iceberg…* (forgiveness, understanding,
     courage, patience; the "pimple" analogy, where the flaw looms larger to you
     than to anyone else).
   - Ch. 22: Walter H. Manning, *Finding Your Own Path Without Professional Help*
     (the "things I do because I stutter" list; "don't chase the fluency god").
   - Ch. 23: Paul E. Czuchna, *Guidelines* (the covert versus overt stutterer).
   - Ch. 24: Robert W. Quesal, *Knowledge, Understanding, and Acceptance*.
   - Ch. 25: Gary J. Rentschler, *Maintaining Dignity While Living With
     Stuttering* (explaining your stuttering to a listener; the wheelchair
     analogy).
   - Ch. 26: Kenneth O. St. Louis, *Your Life Is Too Important to Spend It
     Worrying About Stuttering*.
   - Ch. 27: Harold B. Starbuck, *Do-It-Yourself Kit for Stutterers* ("the kit
     was empty: you already have the tools").
   - Ch. 28: Charles Van Riper, *Putting It Together* ("there are no magical
     cures… you can change your abnormal reactions").
2. **Stuttering Foundation of America.** Myths and facts, brochures, and
   clinician referral lists. <https://www.stutteringhelp.org>
3. **The Stuttering Homepage** (ed. Judy Kuster), a long-running directory of
   stuttering resources, listed in the source book at stutteringhomepage.com.

The rule about carrying both spellings, "stuttering" and "stammering", is a
Speechworks decision about search and audience (UK and India search behaviour),
not something from the book above. See the Speechworks SEO notes.

---

## Disclaimer

This skill captures communication and brand guidance distilled from the sources
above. **It is not clinical advice, and it is not a substitute for assessment or
therapy by a qualified speech-language pathologist.** Any misreading of the cited
work is the maintainers' alone.

## License

[MIT](./LICENSE) © Speechworks.
