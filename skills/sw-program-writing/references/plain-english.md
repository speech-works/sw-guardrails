# Plain English for Speechworks

These rules were tested in three blind rounds on real Speechworks lessons.
They apply to all program copy and to any other user-facing Speechworks text.

Target reader: an adult with everyday English (about CEFR B1, a reading age of
9 to 11), no clinical training, reading once. Our words are mostly simple
already. Our sentences are the problem: long clause chains, idioms, images
and contrast frames make a reader work twice. The fix changes the sentences
and leaves the meaning, the facts and the warmth alone.

## Procedure for a rewrite

1. **Read the whole text first.** Know what the reader must understand, feel
   or do by the end.
2. **Lock the facts.** Note every number, percentage, year, study, name,
   program title and anything in quotation marks. These do not change. Leave
   quoted research wording and a user's own words as they are.
3. **Edit the least you can.** Mark the sentences that break a hard rule (the
   checker lists most of them). Rewrite those, one at a time. Leave every
   other sentence word for word, even if you would phrase it differently.
   Plain, warm lines the writer already got right are the voice of the
   program.
4. **Check.** Save the original and the rewrite as files and run
   `scripts/check.sh before.md after.md`. Vale errors must be zero and the
   fact lock must pass. Read every "ADDED" line: a definition you added is a
   new claim, so it must be true and, in a lesson, match the evidence entry.
   The fact lock cannot see a dropped idea or a changed meaning. Compare the
   two versions sentence by sentence yourself.
5. **Read it aloud once as the target reader.** If a sentence needs a second
   read, split it again.
6. **Return** the rewrite and a short list of anything you kept complex on
   purpose, with the reason.

For new text (mode A), write to these rules from the first draft and run
`scripts/check.sh new.md` for Vale only.

## Hard rules

1. **20 words at most per sentence.** Aim for 10 to 15 on average. One idea
   per sentence.
2. **At most one join per sentence** (and, but, because, so, which, when).
   Two joins means two sentences. When you split, carry the join word into
   the new sentence ("So", "But", "Because of this"). A split must never drop
   a cause.
3. **No idioms, no figures of speech, no phrasal verbs where a single verb
   exists.** "Hold the number loosely" becomes "Treat the number with care".
   "Set it off" becomes "start it".
4. **Named images stay, and get explained.** Speechworks uses a few pictures
   on purpose: the iceberg, the metronome, the alarm, the arrow (which way
   cause runs), the timing circuit. Keep the picture and add one plain
   sentence that says what it means. Never delete one, and never add a new
   one.
5. **No contrast frames.** No "not X, but Y", no "It is not X. It is Y.", no
   "rather than", no "instead of" used as a contrast, no trailing ", not Y".
   Say the positive point once. Test a negation by deleting it. If the reader
   would now keep a common myth ("nerves cause stuttering"), put it back,
   once, and state the positive fact in the next sentence. Otherwise leave it
   out.
6. **Facts and hedges are locked, including their reach.** Same numbers,
   studies, limits and hedges. When you split a hedged sentence ("The
   explanation says the circuit starts each piece of speech"), every new
   sentence keeps the hedge ("In this explanation, the circuit..."). A fact
   must never escape its hedge. Never make a finding stronger or weaker. Do
   not add or drop hedge words (yet, still, usually, often, may, about,
   roughly, a proposal, a model). "Still a proposal" must not become "not yet
   a settled fact": "yet" promises proof. Never strengthen a negation: "not
   about you" must not become "nothing about you", and "not caused by nerves"
   must not grow into a longer list of things it has "nothing to do with".
   "Not a diagnosis of anybody" must not become "cannot diagnose any person".
7. **Keep what a negation protects.** When you remove a contrast frame, the
   negative half often guards against shame or a myth. Keep that meaning,
   said plainly. "Skipping a day is a choice, not a miss" becomes "Skipping a
   day is a choice. It does not count against you." Never leave a bare "This
   is not about nerves." that the next paragraph contradicts.
8. **Same emotional temperature, one meaning.** Swap a word only for one of
   the same or lower intensity. "Assessing" does not become "judging", "your
   heart going" does not become "racing", "managing a secret" does not become
   "hiding", "has the same shape" does not become "makes the same mistake".
   Never make a neutral phrase blame someone ("nobody checked this"). Each
   plain phrase must have only one reading: "relaxing is fine by itself" can
   mean "relaxing alone is enough", so write what you mean.
9. **Keep "you" and the warmth.** Keep every line of kindness, choice and
   permission ("If today is not the day, skip it"). A clear lesson that feels
   cold has failed.
10. **House style.** No em or en dashes as punctuation. No AI vocabulary
    (delve, crucial, journey, empower, navigate, foster, unlock, genuinely).
    Always "Speechworks". Use "stammer" and "programme" only in text meant for
    UK and Irish readers.
11. **Definitions must be complete and true.** Use the wording in
    `approved-definitions.md`. If the program already defines the term in an
    earlier day, that definition wins. The day's own numbers and hedges
    always win. If you must write a new definition, flag it for a clinician.

## Strong defaults

12. **Rhythm.** Mix sentence lengths between about 8 and 20 words. Do not
    stack three or more very short sentences; join them. Never leave a short
    orphan sentence ("That is useful to know.") after a split; join it to the
    sentence next to it. Do not explain a picture the reader already
    understands. No signpost lines ("Two points need care."). Merge repeated
    parallel sentences into one list. Keep a rewrite within 10% of the
    original length. No filler openers ("Let us look more closely").
13. **Common words first.** "Use" over "utilise", "start" over "initiate",
    "about" over "approximately". If a technical term helps the reader, give
    the plain meaning the first time: "safety behaviours, the things people do
    to get through a hard moment".
14. **Verbs over abstract nouns.** "When you disclose" over "disclosure
    behaviour".
15. **Active voice** when it names who does what. A clear passive can stay.
16. **Report research in this order:** who was studied, what they did, what
    they found, the limit. One number per sentence. Prefer natural frequencies
    ("6 in 10 people") to percentages.
17. **Instructions:** condition first, then the action, then one reason. "If
    the call feels too big, say your answers out loud instead."
18. **Paragraphs of 3 sentences,** never more than 5. One topic each.
19. **Lists for 3 or more parallel items** in instructions. Keep flowing prose
    in teaching, where lists would feel cold.
20. **Numbers:** keep the form the text already uses. Words read warmly for
    small numbers ("six in ten"); use numerals for 10 and above and for data.
    Never change a number's value.

## What not to do

- Do not add facts, examples or reassurance that were not there.
- Do not turn a lesson into bullet points throughout.
- Do not make it childish. Short sentences, adult ideas.
- Do not grade by readability formula alone. Formulas disagree by several
  grade levels. The hard rules and the read-aloud check are the test.

## Contrast frames: how to rewrite them

- "It is not a character flaw. It is a common pattern." becomes "This is a
  common pattern. Many people who stutter share it."
- "Choose the word you mean rather than the safe one." becomes "Choose the
  word you mean, even if it feels harder to say."
- Keep a correcting negation when the reader likely believes the opposite:
  "Nerves do not cause stuttering. It starts in how the brain times speech."

## Words to swap

| Instead of | Write |
|---|---|
| approximately | about |
| utilise | use |
| individuals | people |
| demonstrate | show |
| sufficient | enough |
| subsequently | later, then |
| in order to | to |
| associated with | linked to, found with (same strength, never a cause word) |
| self-reported | people said |
| participants | people in the study |
| disclosure | telling people (keep "disclosure" in The Art of Disclosure title and explain it once) |

## Why each rule exists

| Rule | Why | Source |
|---|---|---|
| 20 words at most, 10 to 15 on average | Long sentences were the main barrier in our own audit (12 to 30% of lesson sentences). A house convention: PROGRAM_STRATEGY 4.4 notes no study sets the number. | NHS content guide; GOV.UK splits at 25 |
| One join per sentence | Clause chains force the reader to hold several ideas at once | Our audit; US Federal Plain Language Guidelines |
| Carry the join word when splitting | Causal markers help first and second language readers | PROGRAM_STRATEGY 4.4 |
| No idioms or figures of speech | Second-language readers guess idioms and often guess wrong | Cooper 1999, TESOL Quarterly 33(2) |
| Explain named images once | The iceberg and the metronome carry meaning; deleting them loses it | Our test of easy-language, which deleted the metronome |
| No contrast frames | "rather than" appeared about 350 times and "It is not X. It is Y." 58 times; readers must hold the wrong idea to reach the right one | Our audit; house style |
| Facts locked | A plain rewrite that changes a finding is a clinical error | ProgramEvidence.ts rules |
| Plain term first, technical term after | Readers search and talk in everyday words | NHS ("piles (haemorrhoids)") |
| Natural frequencies | "6 in 10" is understood better than "60%" | Akl et al. 2011, Cochrane review |
| No grading by formula alone | Formulas disagree by up to 5 grade levels on the same text | Redish 2000; Wang et al. 2013 |
