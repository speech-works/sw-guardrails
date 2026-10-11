# Video-locked terms and steps

Eleven program days have a live video. The video's words and captions were
checked against the day's text, step by step. If the text changes a term the
video says out loud, or a step moves, the reader sees and hears two different
things. Required reading for mode C, and for mode B when the program has a
video.

Live captions: `/Users/mayankav/Desktop/SpeechWorks Videos/new/<title>/Character refresh/captions.srt`.
Speech-to-text of each video: `docs/programs/video-audit-2026-09-22/evidence/*-asr.json`.
The 18 files in `docs/video-scripts` are retired. Do not use them as a
reference.

## Rules

1. **In a program with a video, never add, move or remove any step,** the
   VIDEO step included. The step count and order stay as they are. Seven
   programs have one: Understanding Your Voice; The Art of Disclosure; The
   Word Swap; Bouncing Back; Dating, Intimacy & Vulnerability; Interview
   Ready; The Speech Toolkit. The video audit also counts every step in
   every program, so a new program or a new step anywhere needs the video
   check in rule 4.
2. **Keep every term below word for word**, in the teaching, the quiz and the
   activity text of that day, and in any later day that refers back to it.
3. Before renaming any other term on a video day, search the captions and the
   speech-to-text files for it.
4. **After any pack file change, run the video check yourself.** There is no
   separate video team (founder, 2026-10-06). `node scripts/videoImpact.cjs`
   lists every video day whose text changed since the baseline. For each,
   `--show "<title>"` prints the caption next to the day text. Read both and
   check sequence, terms, cross-references and claims. Report what you found.
   Record a new baseline (`--record --note "..."`) only after that reading,
   never to make a failure go away, and ask the founder first.
5. Never edit `docs/programs/video-audit-2026-09-22/replacement-manifest.json`
   or re-hash its files without asking. `preflight.cjs` in that folder is an
   older check that already failed before October 2026, so a failure there
   does not by itself mean your change broke it.

## Terms, by day

| Program, day | Keep word for word |
|---|---|
| Understanding Your Voice, day 1 | Joseph Sheehan; iceberg; "two short lists"; "You do not need to draw an iceberg" |
| The Art of Disclosure, day 1 | 338; informative / apologetic / no disclosure; mirror; three styles; five times (on day 2) |
| The Word Swap, day 1 | swap; "keeping that picture true"; notice without changing (on day 2) |
| Bouncing Back, day 1 | "last two weeks"; "the hour before"; "That day I had also" |
| Dating, Intimacy & Vulnerability, day 1 | "Do not mention it"; "Definitely mention it"; "agreed" |
| Interview Ready, day 6 | situation / what you did / what happened, in this order; "Let me think about that for a second."; two pieces of work, one that "went wrong and got fixed"; saying answers out loud as the alternative. Keep the text's "six weeks" example separate from the video's example. |
| The Speech Toolkit, day 1 | extra moves; day seven; face and shoulders |
| The Speech Toolkit, day 2 | hhh-apple, h-apple, apple, in that order; the h does not stay in the word; lips or tongue still close; less pressure; vowel words before consonants |
| The Speech Toolkit, day 4 | beat; "Before the video"; three conversations; the chosen test |
| The Speech Toolkit, day 5 | chunking; "I am going / to the store / to buy some bread"; three or four words; both test questions; easier reading can still fail the meaning test |

## Notes checked against the captions

- "less press, not less contact" is Speech Toolkit day 2 TEXT, not a video
  line. The text may rewrite it in plain form (less pressure; lips or tongue
  still close). It must not contradict the video.
- "three styles" is what the Art of Disclosure day 1 video says, and "easy
  onset" and "light contact" are what the Speech Toolkit videos say. Since
  2026-09-27 the text uses these words too. Keep them, so readers hear and
  read the same thing.
- After a text change, Claude runs the caption-vs-text check itself (founder,
  2026-09-27): sequence, every "today / tomorrow / later" reference, and every
  term or number the video says. Ask the founder before touching the
  manifest or preflight.cjs.
- The full line-by-line map of what each video refers to is in
  video-crossrefs.md. Check it after every rewrite.
