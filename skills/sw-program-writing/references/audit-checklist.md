# The audit layer

Used by mode B (a new program before it ships) and mode C (an existing
program). Run the steps in order. A step passes only when its pass line is
met. Commands run from the sw-be-2 root unless they start with `<skill>/`,
which means this skill's folder.

## 0. Set up

```bash
npm run build
node <skill>/scripts/extract_program.cjs --repo=. --program=<key> --out=<scratch>/after
node <skill>/scripts/extract_program.cjs --repo=. --all --out=<scratch>/all
```

In mode C, extract the program before you edit (`--out=<scratch>/before`) so
every day has a before and an after file. The extractor marks each block with
its step number, type, role and evidence keys, and shows every quiz question
with its options and explanations. Shared promises show as
`[SHARED:NAME]`.

If the program has a video, read `video-locked-terms.md` now.

## 1. Plain English

```bash
<skill>/scripts/check.sh <scratch>/after/<key>/day-03.md                                  # new text
<skill>/scripts/check.sh <scratch>/before/<key>/day-03.md <scratch>/after/<key>/day-03.md  # a rewrite
```

**Pass:** Vale errors 0 on every day. Fact lock PASS on every rewritten day.
Every ADDED line is true and matches its evidence entry. Every Vale warning
(sentence length, clause chain, idiom, research jargon, trailing negation) is
fixed or has a one-line reason in your report. Then compare each changed
sentence with its original for a dropped idea, a hedge that lost its reach,
a hotter or colder word, or a strengthened negation. The fact lock cannot see
those.

Also check the day title and description by hand: a description is always
plain (strategy 4.3).

## 2. Structure

```bash
node scripts/packDepthReport.cjs --program=<key> --days
npm run content:check
npx jest src/tests/dayCopy.seed.test.ts src/tests/programEvidence.seed.test.ts \
  src/tests/programEndsOnAct.test.ts src/tests/goalHarness.seed.test.ts
npm run spec:tables
```

`content:check` includes the floor (`packDepth`), the quiz bank rules
(`programQuiz`), the answer key (`quizAnswerKey`), answer position and length
bias (`quizAnswerBias`), referential integrity, keepsakes and drill overrides.
`dayCopy`, `programEvidence`, `programEndsOnAct` and `goalHarness` are
outside it, so run them by name.

**Pass:** the depth report exits 0 with 0 days below the floor, and each
bridge in and bridge out sits inside its word range. Every test is green.
The spec's "Day by day, as seeded" table is regenerated and matches the day
list in the spec. A new program is added to `REBUILT` in
`packDepth.seed.test.ts`. A derived duration of 12 to 17 minutes is
accepted; the minutes are information and never a reason to cut.

## 3. Evidence

For every sentence that reports research, a number, a study or a finding:

- the TEXT block's `sources` lists a key for it;
- the sentence carries that entry's `plainCount`, or a count that matches it;
- the claim stays inside the entry's `population`, `design` and `strength`;
- where the sentence could be read wider, the day states the limit as
  `theLimitInPlainWords` says it;
- the wording uses the certainty ladder and no cause word for a link.

```bash
npm run evidence:review
grep -rn "<KEY>" src/seed/pack   # every day that uses an entry you changed
```

**Pass:** 0 unmapped research sentences. 0 claims past population or
strength. 0 claims from the folklore or never-cite lists in `evidence.md`.
The review sheet regenerates without errors. Every day that uses a changed
entry has been re-read.

## 4. Program judgement

The seven questions from strategy 10.3:

1. Does every day have one main message, written down in the spec?
2. Does every quiz item test that day's stated objective?
3. Does the arc use the content bank before writing anything new?
4. Does day 1 end on something the user did and finished?
5. Does the last day give back an accurate account, and something that
   points forward?
6. Does any copy congratulate fluency, praise the person, or shame
   concealment?
7. Does every claim in the sales copy (title, description, day 1) survive
   strategy 8.2?

The faults the 2026-09-05 audit found, which must not come back:

| Fault | Check | Pass |
|---|---|---|
| The bridge in gives away the recall answer | Read each bridge in against the recall pool under it. Look for the answer, its reason, and any detail the distractors turn on ("only once", "with a real person", "three of them"). A wording match is not enough; 45 of 70 leaked in meaning. | 0 leaks. A pair that cannot be cleaned is listed as narrowed. |
| A log that cannot record what the day says it records | The FORM's fields against the block title and the day's words about it | The form has a field for every thing the day says the reader writes down. No `EXPOSURE` form on a paid day. |
| A library activity row that contradicts the day | Read the drill screen text (instructions, encouragement, completion prompt) of every ACTIVITY | No banned instruction, no fixed script the day rejected, no completion gated on anxiety dropping. Fix with overrides or a private `PROG_DRILL_*` row. |
| A promise of readback the product cannot do | Search for "look back at", "your notes from", "review rather than a blank page" | Only keepsake forms and `WEEK_REVIEW` read back. |
| Boilerplate copied between programs | `python3 <skill>/scripts/shared_runs.py <scratch>/all` | New program: 0 ACROSS passages except quoted study wording and technique names. Rewrite: no ACROSS passage that was not there before. |
| Positioning repeated ("this program never", "on purpose", "deliberate", "the honest version", "What this is not") | `grep -n -i` over the extracted days, and the INSIDE lines from `shared_runs.py` | Once per program, on day 1, via the shared promises. 0 elsewhere. |
| A research claim one rung above its label | Step 3 | 0 |
| Synonym cycling | Read for one thing named several ways (swap / trade, forecast / prediction) and for scales that change (out of 10, 0 to 100) | One term, one scale |
| Metaphors that carry meaning, region-locked words, unglossed terms | Vale Idioms warnings plus a read | Named images only, each explained once. Every specialised term glossed where it first appears. |

**Pass:** all seven questions answered yes (question 6: no), with the day
and block named for every no. Every fault row passes.

## 5. Video guard

Only for a program with a video, and for any new program or new step.

**Pass:** 0 locked terms changed (search the before and after files for each
term in `video-locked-terms.md`). The step count and order are unchanged in a
program with a video. Your report says, in one line, that the video team
must re-run its text-to-caption comparison, and names the pack files you
changed. You did not touch the video manifest.

## 6. sw-guardrails review

Run the sw-guardrails skill on every changed or new day, including titles,
descriptions, quiz explanations and drill overrides.

**Pass:** 0 block (red) findings. Each warn (amber) finding is fixed or has
a written argument. Notes are listed in the report.

## 7. The blind three-reader test

Three subagents, run separately. Give each only the inputs in its row: no
spec, no author notes, no rationale, no earlier reader's answer. In mode C
the "before" file is the extracted original day. After a fix, run the failed
reader again as a new agent.

| Reader | Brief | Gets | Pass |
|---|---|---|---|
| Non-native reader | "You are an adult who reads English at about CEFR B1, with no clinical training. Read the day once. Mark every sentence you had to read twice or could read two ways. Then say in your own words what the day wants you to understand and what it asks you to do." | The day text only | Main message and task restated correctly. At most 1 marked sentence per day, and none in a task instruction or a quiz question. No idiom read literally. |
| Clinician fact-check | "You are a speech and language therapist who checks research claims. List every claim that is stronger or weaker than its evidence entry, every dropped hedge or limit, every definition that is wrong or incomplete, and every claim of cure, treatment or a fluency outcome." | The day text, its evidence entries, and in mode C the before text | 0 errors of any kind. One error fails the day. |
| Founder warmth | "You wrote this program for adults who stutter. Score its warmth from 1 to 5. List any line of permission, choice or kindness that is missing, any word that became colder or hotter, any praise of the person, and anything that reads as generated." | The day text, and in mode C the before text | Score 4 or 5, and in mode C not lower than before. 0 lost permission or kindness lines. 0 colder swaps. 0 person praise. |

If this step leads to any change, run steps 1 and 6 again on the changed
lines.

## The report

Return, in this order:

1. The verdict per step: pass or fail, with the number behind it.
2. Each finding: program, day, step number, the rule it breaks, the text,
   and the fix (or "needs founder", "needs clinician", "needs product
   change").
3. In mode C, the changed lines with the rule behind each, and anything kept
   complex on purpose.
4. The video team line, if step 5 applied.
