# Program design: the rules a writer needs

Extracted from `docs/programs/PROGRAM_STRATEGY.md` in sw-be-2. That doc is the
authority. Where this file and the doc disagree, the doc wins; tell the user
so this file gets fixed. Section numbers below are the doc's parts, so you can
read the evidence behind a rule before you argue with it.

The doc marks each rule EVIDENCE (a study survived checking) or DECISION (a
choice we made). Both are binding. Do not dress a decision in a citation (Part
0).

## Research and spec (Part 2)

- Name the pain in the user's words, in one sentence (2.1 step 1).
- Research through three lenses kept apart: clinical, psychological, lived
  experience. Where they disagree, the spec records the choice (2.1 step 2).
- Primary sources only. Label every finding STRONG, MODERATE or WEAK and name
  its population. Lived experience is authoritative about what patronises. It
  is no evidence of effect. Record what nobody has measured (2.1 step 3).
- A person or subagent who did not write the research tries to break it
  (2.1 step 4). "I could not fetch this" does not mean "this is wrong".
- Write what the program may and may not claim before any day (2.1 step 5).
- Spec at `docs/programs/specs/<catalogKey>.md`, ten sections: why it exists;
  what the content bank already has; the through line; the user's own goal;
  the keepsake and which day feeds which line; day by day; the three moments;
  before and after; safety notes; sources with strength labels (2.2).
  `art_of_disclosure.md` is the template. `npm run spec:tables` adds the
  generated "Day by day, as seeded" table, which wins over the prose above it.

## The day (Part 3)

**The floor (3.2)**, checked by `packDepth.seed.test.ts` for every pack with a
`catalogKey`: at least 6 blocks, 350 teaching words, 1 ACTIVITY, 1 FORM; a
recall quiz and opening recap from day 2; a check quiz and a bridge out every
day; never all TEXT.

**The spine (3.3):**

| # | Block | Job | Size |
|---|---|---|---|
| 1 | Bridge in (TEXT, `role: "bridge_in"`) | Yesterday's act turned into today's starting point. Day 1 frames the arc. | 60 to 90 words |
| 2 | Recall (QUIZ, `mode: "recall"`) | One question on yesterday, from a pool of 3 to 5 keys | day 2 on |
| 3 | Teach (TEXT, `role: "teach"`) | The day's real teaching | at least 200 words |
| 4 | Check (QUIZ, `mode: "check"`) | Every key asked, about today | at least 2 |
| 5 | Do (ACTIVITY) | A rep aimed at something the user named at intake | at least 1 |
| 6 | Log (FORM) | What happened. Usually feeds one keepsake line. | at least 1 |
| 7 | Bridge out (TEXT, `role: "bridge_out"`) | What today set up, and what tomorrow does with it | 40 to 60 words |

- Extra blocks are welcome (VIDEO, GOALS, WEEK_REVIEW). Never teach after
  asking, and never leave a day without a record.
- The last day ends on an ACTIVITY: `... ACTIVITY, FORM, bridge out, ACTIVITY`
  (`programEndsOnAct.test.ts`).
- If tomorrow's task involves another person, today's bridge out names it
  plainly. Say what it is. Do not add reassurance the day has not earned
  (3.4, a DECISION).
- The renderer handles headings `#` to `####`, blockquotes (`> ` on every
  line), checkbox, bullet and ordered lists, bold, italic, links. No tables,
  images, code blocks or nested lists (3.9).
- Pick a teaching format: cited excerpt with critique, two-source contrast,
  annotated transcript, worked example, myth against evidence, checkbox
  worksheet, bank activity, AI call rep. Never plain prose from start to end
  (3.10).
- One behaviour, one concept per day (3.11).
- Write in this order: objective, then the quiz item that proves it, then the
  teaching (3.12). A question about something stated three paragraphs up is a
  recall question, whatever its verb.
- Show a worked example before independent practice when a technique is new,
  and fade guidance slowly (3.13).
- Every day stands alone: a user who does days 1, 2 and 5 still gets
  something (3.14).
- Duration is derived by `scripts/packDepthReport.cjs` (3.7). Set
  `estimatedMinutes` on an activity when the type default is wrong. Days are
  never cut to hit ten minutes; a long day gets better material (3.8,
  superseded by founder decision 2026-09-05).

**The task (3.15):**

- So exact that "did I do it?" has a yes or no answer: who, where, what
  sentence, how long.
- Name the fear tier. High-fear reps are attendance or observation, never
  performance. The first rep of a program is never a speaking task.
- Two to four real choices, never cosmetic variants.
- A prediction before and the outcome after.
- An if-then plan in the user's own words.
- Never gate progress on anxiety dropping.
- Early days set learning goals ("find two situations where you can say your
  name and stay in the block"). Performance goals come later, if at all.
- An opt-out in the task's own words on every rep. Skipping is never failure.

**The log (3.16):** mandatory and it closes the day; at most 26 fields; at
least one field records what happened; ask why; concrete and forward-closing,
never a rumination surface; never name the feeling ("How much shame did you
feel?" fails, "What happened?" passes). Use the program log forms
(`PROGRAM_REP_LOG`, `PROGRAM_WILLINGNESS`, `PROGRAM_BELIEF_EXPERIMENT`,
`TOOLKIT_TRIAL_LOG`, `POST_EVENT_LOG`). The retired `EXPOSURE` form has no
expected or happened field; never put it on a paid day.

**Readback is limited.** Only keepsake forms and the last-day `WEEK_REVIEW`
block show the user their own record. Do not promise a readback anywhere
else.

**Activity rows are shared.** A library activity row also shows in Explore
and in free packs. Change what a paid day shows with `titleOverride`,
`descriptionOverride`, `instructionsOverride`, `encouragementOverride`,
`completionPromptOverride` and `completionPlaceholderOverride`, or write a
private `PROG_DRILL_*` row. Read the drill screen text: it is what the reader
sees just before they act.

## Copy (Part 4)

**Never (4.1):** congratulate fluency or smoothness; praise the person ("you're
brave"; praise the action: "You did", "You tried"); "relax", "slow down",
"take a breath" as instruction; "should", "must", "have to", "need to", "got
to" in an instruction; end feedback with an exhortation ("keep it up"); guilt
or loss framing for a missed day; any cure word ("overcome", "beat", "fix",
"stop stuttering", "ex-stutterer"); stutter or stammer as a metaphor; treat
concealment as a fault; count or log stuttering frequency; em dashes, idioms,
trailing ellipses, business jargon, AI writing tells.

**Always (4.2):** one main message per day, written before drafting; second
person, one reader, active voice; a one-sentence reason under 25 words for
every instruction; name the difficulty honestly ("This one is hard, and a lot
of people find this week the worst"); say what to do; the same term for the
same thing every time; explain a specialised term where it first appears; no
acronyms, no "e.g.", "i.e.", "etc.", no region-locked terms; structure and
autonomy together.

**Titles and descriptions (4.3):** a day title may name a model the day
teaches. A description is always plain. Both render before purchase, so this
is the highest-stakes copy. `dayCopy.seed.test.ts` holds it, with a ratchet of
phrases already removed once.

**Reading level (4.4):** target reading age 11, used as a flag, never a gate.
The binding check is vocabulary: about 7 unfamiliar words per 350, each one a
term being taught and glossed at first use. Repeat a term; do not cycle
synonyms. Keep connectives.

## The quiz (Part 5)

- Questions live in `src/seed/question/programQuiz.ts`. `shortId` is
  `<program>_d<day>_<r|c><n>` and names the day it tests. No database ids in
  seed or block payloads (5.1).
- Exactly three options: one right answer, two distractors the reader could
  argue against from today's text (5.2).
- An explanation on every option: the right answer, why, and why the chosen
  distractor is wrong. Two or three sentences. Address the answer, never the
  person. No score, no praise.
- Never "all of the above" or "A. 1 and 2". Avoid "none of the above".
- Item vocabulary at or below the teaching text's.
- Say the quiz has no stakes.
- The recall question is about yesterday only. The bridge in must not state
  its answer, its reason, or the detail the distractors were built on.
- Vary the right answer's position and length.
  `quizAnswerBias.seed.test.ts` fails both "always" and "never".
- Block by topic, space by day. Do not interleave topics.

## The three moments and the keepsake (Part 6)

- **Day 1:** a finished action in the user's own voice, under ten minutes; a
  line that says "You just did X, which is what this program is for"; one
  finished artifact.
- **The middle:** change the shape (a new exercise type, a new context, or the
  first real-world attempt); self-monitoring plus goal review. No simulated
  people, no fake counts of other users.
- **The last day:** an accurate, specific account of what changed, on a
  dimension the user chose and rated; the day 1 artifact back, extended;
  if-then plans for the weeks after; end on the user's own action; label it
  the last day. Never a fluency comparison.
- **Never build:** a streak that can break, leaderboards, badges as the main
  scaffold, fake social presence, "most people do this" norms, loss framing.
- **The keepsake** is built a line at a time across the week and finished on
  the last day. Never scored, never shown to anyone else.

## Excerpts (Part 7)

Our own teaching prose is fine. Paraphrase research with a citation. Never
present invented text as someone's words. Literary excerpts only if first
published 1930 or earlier and the author died more than 70 years ago. Every
quotation names the source and the author.

## Claims and safety (Part 8)

- Promise the program, specifically. Never promise anything about the stutter
  (8.1). Example: "Seven days. Seven real speaking situations, in your own
  voice."
- Never: a fluency outcome; "treatment", "therapy", "clinical",
  "intervention", "assessment" or "diagnosis" for the product; a number we
  have not measured; "you will feel" claims; OASES items or reworded ones;
  "causes" or "improves" for a finding that only shows a link; "breakthrough",
  "cure", "miracle", "proven" (8.2).
- Use the certainty ladder: causes / probably / may / it is unclear whether.
- Assume many readers have an anxiety disorder. Nothing detects distress
  inside a program, so write every day as if nothing does. The shared
  `RESOURCES_ROUTE` promise carries the route to a person (8.3).
- No jurisdiction-specific advice, including workplace rights.

## Enriching an existing program (Part 9)

Measure, read for what it gets right, inventory the content bank, research if
none exists, write the spec, write the quiz bank, write the days, measure
again, and add the program to `REBUILT` in `packDepth.seed.test.ts` last.

## Shared copy

`src/seed/pack/sharedCopy.ts` holds five promises that must be word for word
the same in every program: `RESOURCES_ROUTE`, `SKIP_IS_A_CHOICE`,
`PRIVATE_AND_UNSCORED`, `THERAPY_EXISTS` and `THIS_PROGRAM_WILL_CHANGE`.
Import them. Never paraphrase them. Everything else must be written for its
own program.

## Where the two standards meet

The plain-English rules and PROGRAM_STRATEGY.md pull in different directions
in five places. This is how the skill settles each one.

| Point | Strategy says | Plain-English rules say | Resolution |
|---|---|---|---|
| Connectives | Keep them; splitting usually deletes one (4.4) | One join per sentence; split long ones | Split, and carry the join word into the new sentence ("So", "But"). Never drop a cause. |
| Sentence length | No evidence for a 20-word ceiling; a convention (4.4) | Hard rule: 20 words at most | Keep 20 as a house DECISION. Vale warns; a sentence over 20 needs a written reason. |
| Research verbs | Say "associated with", never "causes" (8.2) | "associated with" is jargon; use "linked to" | Use "linked to" or "found with". Same strength, never a cause word. The certainty ladder still applies. |
| Images | No metaphors that carry meaning (4.1) | Named images stay and get explained | The named images (iceberg, metronome, alarm, arrow, timing circuit) are taught terms with approved definitions, and some are spoken in videos. Keep them, explain once, add no new ones. |
| Negations | Day 1 states what the program does not do; say it once (audit 1.5) | No contrast frames | The day 1 shared promises keep their negations because they guard against a myth or shame (plain-English rule 7). Say them once, on day 1, and nowhere else. |

Two smaller points: the strategy's reading age 11 is the top of the
plain-English target of 9 to 11, so aim at 9 to 11 and flag above 11. The Vale
vocabulary accepts "CBT" and "SLP" so they do not show as spelling errors;
reader copy still spells them out (4.2, no acronyms).
