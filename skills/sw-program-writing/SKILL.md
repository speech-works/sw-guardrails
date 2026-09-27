---
name: sw-program-writing
description: >-
  Write and audit Speechworks programs. Use it to write a new program or a new
  day from scratch (research, evidence entries, spec, quiz bank, then days
  built on the spine), to edit any program copy (lessons, bridges, quiz questions
  and explanations, activity and form overrides, day titles and descriptions,
  evidence plainCount and limits), to audit a newly written program before it
  ships, and to audit and rewrite an existing program with the smallest edit.
  Also use it to make any program text plain English for adults who may read
  English as a second language. Keeps facts, hedges and video-locked terms
  exactly, and checks the result with Vale, a fact lock, the sw-be-2 structure
  tests and a blind three-reader test. Triggers: "write a program", "add a
  day", "draft day 3", "edit this lesson", "audit this program", "is this
  program ready to ship", "make this plain English", "simplify this lesson",
  "too complex", "check reading level". Calls for a sw-guardrails review of
  the final copy.
---

# Speechworks program writing

Speechworks programs are paid, day-by-day courses for adults who stutter. Many
readers use English as a second language, and many are tired or anxious when
they read. Every day must teach one thing, ask the reader to do one thing, and
record what happened, in plain English that works on the first read.

The full standard is `docs/programs/PROGRAM_STRATEGY.md` in sw-be-2. This skill
carries the rules a writer needs and points to the doc for the reasons. All
paths below are relative to the sw-be-2 repo. Script paths are relative to
this skill's folder.

## Pick the mode

| The request | Mode |
|---|---|
| A new program, a new day, or a new block that does not exist yet | **A. Write** |
| A program or day written recently that has not shipped | **B. Audit new** |
| A live program: audit it, edit it, simplify it, fix a reported fault | **C. Audit and rewrite** |

If you cannot tell whether the text is live, check the pack for a `catalogKey`
and ask. Modes B and C share one audit layer, described below and in full in
`references/audit-checklist.md`.

## Rules for every mode

1. **Plain English from the first draft.** Follow the hard rules in
   `references/plain-english.md`: at most 20 words and one join per sentence,
   no idioms, no contrast frames, facts and hedges locked with their reach,
   the same emotional temperature, definitions complete and true.
2. **Every research claim has an evidence key.** The TEXT block lists it in
   `sources`, the sentence carries the entry's `plainCount`, and the claim
   never goes past the entry's population or strength. See
   `references/evidence.md`.
3. **Every day follows the spine and meets the floor.** Bridge in, recall,
   teach, check, do, log, bridge out. See `references/program-design.md`.
4. **Copy rules from Part 4 of the strategy.** Never praise fluency or the
   person, never tell a reader to relax, slow down or breathe, no "should",
   "must" or "need to" in an instruction, no cure words, no streaks, no guilt
   for a missed day, never name the feeling for the reader.
5. **Say the positioning once.** The day 1 promises come from
   `src/seed/pack/sharedCopy.ts`. Do not repeat "this program never" or "on
   purpose" lines, and do not copy paragraphs from another program.
6. **House style.** No em dashes, no "not X, but Y", no AI vocabulary, and
   always "Speechworks". Follow `references/examples.md` for tone and length.
7. **Video-locked terms and steps.** In a program with a video, never add,
   move or remove a step, and keep every term in
   `references/video-locked-terms.md` word for word. Read that file before
   any mode B or C work on such a program. After any pack file change, tell
   the video team. Never update their manifest hashes yourself.

## Mode A: write a new program or day

1. **Name the pain** in one sentence a user would recognise: a situation, never
   "confidence".
2. **Research pass** through three lenses kept apart: clinical, psychological,
   lived experience. Label each finding STRONG, MODERATE or WEAK, name its
   population, and record what nobody has measured. Ask a subagent that did
   not write it to try to break it. Pull abstracts with PubMed E-utilities
   (`references/evidence.md`).
3. **Write what the program may and may not claim** (strategy Part 8) before
   any day.
4. **Evidence entries.** For each claim, reuse a `ProgramEvidence` key or add
   one with every required field, including `plainCount`,
   `whatItDoesNotShow`, `theLimitInPlainWords` and an honest `sourceRead`.
   Add its `ProgramEvidenceRationale` entry in the same change.
5. **Spec** in `docs/programs/specs/<catalogKey>.md`, with the ten sections of
   strategy 2.2. Copy the shape of `art_of_disclosure.md`. Inventory the
   content bank first and reuse activities and forms before writing new ones.
6. **Per day, in this order:** the main message in one to three sentences,
   the objective, the check questions that would prove it, then the teaching.
   If you cannot write the check, you do not yet have an objective.
7. **Quiz bank before the days.** About 40 questions for 7 days: 2 or 3 check
   questions per day, and a recall pool of 3 to 5 per day from day 2. Exactly
   three options, an explanation on every option, and the right answer moved
   around in position and length.
8. **Write the days on the spine.** The bridge in names what the reader did
   yesterday and never states a recall answer. The log records what happened.
   The bridge out names tomorrow's real-world task if it involves another
   person.
9. **Run the audit layer**, then fix and run it again until every step passes.

## Mode B: audit a new program

Run the whole audit layer. Report each finding with its day, block, the rule
it breaks and a fix. Fix what you were asked to fix, then run the failing steps
again. A new program ships only when every step passes.

## Mode C: audit and rewrite an existing program

1. **Measure.** Build, then
   `node scripts/packDepthReport.cjs --program=<key> --days`.
2. **Extract and read.** `node <skill>/scripts/extract_program.cjs
   --repo=<sw-be-2> --program=<key> --out=<scratch>/before` writes one file
   per day. Read all of it, with the spec and the evidence entries. Write down
   what the program gets right. That stays.
3. **Lock.** Numbers, studies, hedges, quoted wording, evidence keys, shared
   promises, video-locked terms, and the step count and order in a program
   with a video.
4. **Mark, then edit the least you can.** Mark the sentences that break a hard
   rule or a program rule. Rewrite only those. Leave every other sentence
   word for word, even if you would phrase it another way.
5. **Check the pair.** `scripts/check.sh before.md after.md` for each changed
   day, then run the audit layer.
6. **Return** the changed lines with the rule behind each, anything you kept
   complex on purpose, and faults you found and did not fix because they need
   the founder, a clinician or a product change.

## The audit layer

Run in this order. Every step has a pass line. Commands and details are in
`references/audit-checklist.md`.

| # | Step | Pass |
|---|---|---|
| 1 | Plain English: `scripts/check.sh` on each day (Vale, plus the fact lock for a rewrite) | Vale errors 0. Fact lock PASS. Every ADDED line is true and matches its evidence entry. Each Vale warning is fixed or has a written reason. |
| 2 | Structure: depth report, `npm run content:check`, the copy, evidence and last-day tests, `npm run spec:tables` | 0 days below the floor. All tests green, including `quizAnswerBias`. Spec table regenerated. |
| 3 | Evidence: every research sentence has a key, `plainCount` in the sentence, the limit kept; `npm run evidence:review` | 0 unmapped claims. 0 claims past population or strength. Review sheet regenerated. |
| 4 | Program judgement: strategy 10.3 questions and the past faults (recap leaks, generic logs, boilerplate, repeated positioning) with `scripts/shared_runs.py` | 0 recall answers in a bridge in. No new passage shared with another program. Each repeat has a reason. |
| 5 | Video guard: `references/video-locked-terms.md` | 0 locked terms changed. Step count and order unchanged in a program with a video. Video team told. |
| 6 | sw-guardrails review of the changed copy | 0 block findings. Each warn finding fixed or argued in writing. |
| 7 | Blind three-reader test (below) | All three readers pass. |

If step 7 leads to any change in the copy, run steps 1 and 6 again on the
changed lines, so sw-guardrails always sees the final text.

### The blind three-reader test

Run three separate subagents. Each gets only the inputs named here, with no
author notes and no rationale. After a fix, run the reader that failed again
as a new agent.

| Reader | Gets | Pass |
|---|---|---|
| Non-native reader: an adult at about CEFR B1, no clinical training, reading once | The day text only | Restates the main message and the task correctly in their own words. At most 1 sentence per day needed a second read, and none in a task instruction or a quiz question. No idiom read literally. |
| Clinician fact-check | The day text, its evidence entries, and in mode C the before text | 0 claims stronger or weaker than the entry, 0 dropped hedges or limits, 0 wrong definitions, 0 claims banned by strategy 8.2. One error fails the day. |
| Founder warmth | The day text, and in mode C the before text | Warmth scored 4 or 5 out of 5, and in mode C not lower than before. 0 permission, choice or kindness lines lost. 0 colder word swaps, 0 person praise. |

## Files

- `references/`: `plain-english.md` (the tested rules), `program-design.md`
  (strategy rules and where the two standards meet), `evidence.md`,
  `audit-checklist.md`, `video-locked-terms.md`, `approved-definitions.md`,
  `examples.md`.
- `scripts/check.sh`, `scripts/fact_lock.py`, `vale/`: the plain-English
  checker. Needs `vale` and Python 3.
- `scripts/extract_program.cjs`: one file per day from the sw-be-2 build.
- `scripts/shared_runs.py`: passages repeated between or inside programs.
- `NOTICE.md`: sources and licences.
