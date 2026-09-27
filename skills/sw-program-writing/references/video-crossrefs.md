# Video cross-references

Every caption line in the 11 live program videos that points at something
outside the video: a step already done, a step still to come, or a task on
the same day. Use this file as a checklist after any rewrite of a program that
has a video. Tick each row only when the program text still makes the caption
line true.

Read it together with `video-locked-terms.md`. That file lists the words to
keep. This file lists the promises the videos make about the program, and
what the program must keep doing for each promise to stay true.

## Sources

- Captions: `/Users/mayankav/Desktop/SpeechWorks Videos/new/<title>/Character refresh/captions.srt`.
  These are the versions named in
  `sw-be-2/docs/programs/video-audit-2026-09-22/replacement-manifest.json`.
- Program text: `sw-be-2/src/seed/pack/*.ts` at commit `bdc55e3`
  (27 September 2026). Activities come from `src/seed/exposure/*.ts` and
  `src/seed/cognitive/index.ts`, forms from `src/seed/form/index.ts`, and the
  Interview Ready call scripts from `src/seed/exposure/interviewReady.ts`.
- Program text was extracted with `scripts/extract_program.cjs`. The quotes
  below are taken from it.

## How to read a row

- **ID** is the video code plus a number, for example `IB2`.
- **Caption** is the exact text, with the start time of its first cue. When
  several caption sentences make one reference, they share a row.
- **Direction**:
  - *backward*: something the user already did or read ("you've just read",
    "yesterday").
  - *forward*: something still to come, on the same day or later ("next",
    "then", "after the short check", "tomorrow", "later", "day seven").
  - *same-day*: the current day's task or text, with no word about order
    ("today you will write", "this lesson").
- **Points to**: program, day and step. "Step" is the block number in the day
  (`orderIndex`), as the extractor prints it.
- **Must stay true**: what a rewrite must keep for the caption to stay
  correct. This covers order, count, task, term, number and example.
- **Today**: holds, broken or unclear, as of commit `bdc55e3`.

Caption lines that are the video's own example, demonstration or research
point, and that do not point at a program step, are not rows. They are listed
under "Shared facts and examples" for each video, because the program must not
contradict them.

## Counts today

| | Rows | Holds | Broken | Unclear |
|---|---|---|---|---|
| Backward | 4 | 4 | 0 | 0 |
| Forward | 38 | 36 | 0 | 2 |
| Same-day | 56 | 53 | 1 | 2 |
| **Total** | **98** | **93** | **1** | **4** |

Broken: IB2. Unclear: IB4, IR5, LC5, P5.

**Update 2026-09-27:** the plain-English rewrite fixed all five (IB2, IB4, IR5, LC5, P5) and closed the term gaps: the text now says "three styles", "easy onset" and "light contact". A caption-vs-text check of all 11 videos found every reference holds. The per-row notes below describe the text as of `bdc55e3`.

## Steps a rewrite must treat as locked

A step on this list is named by a video. Its position, its task and the named
detail must survive a rewrite. Rule 1 of `video-locked-terms.md` (no added,
moved or removed steps in these programs) still applies to everything else.

| Program | Day and step | What the video relies on |
|---|---|---|
| Understanding Your Voice | D1 steps 4, 6 | two lists (noticed, not seen); no drawing |
| | D2, D3, D4 (teaching) | causes, why it varies, explanations you were told, in that order |
| | D5 step 6 | an exercise about noticing effort (see IB4) |
| | D6 step 6 | looking back to find one swap |
| | D7 steps 7, 9 | a card; a reply said out loud, on your own |
| The Art of Disclosure | D1 steps 5, 6 | write one line today |
| | D2 steps 3, 5 | three ways of saying it; mirror; five times; tomorrow |
| | D3 to D6 | try it on people, answer unwanted advice (D5), where the line goes (D6) |
| | D7 step 7 | card that lets a name be marked "no need" |
| The Word Swap | D1 step 6 | two lists, private and written |
| | D2 step 5 | notice a swap, change nothing, tomorrow |
| | D3, D4, D5 (step 5 each) | original word, unplanned exchange, repetition on purpose, in that order |
| | D6 step 3 | a swap you keep is allowed |
| | D7 step 7 | word card has a line for swaps you keep |
| Bouncing Back | D1 step 7 | a day from the last two weeks; sleep, who, rushed, worries; hour-before option; "That day I had also..." |
| | D3, D5, D6 (steps 3 and 5) | plain account, friend version, one review with an end, in that order |
| Dating, Intimacy & Vulnerability | D1 steps 2, 4, 6, 7 | opposite advice on the list; private writing; words, who, agreed, cost; no date |
| | D2 step 4, D3 steps 3 to 7, D4 step 3, D6 steps 3 to 7 | timing; optional line; rejection; replies to interruptions |
| | D7 steps 8, 11 | a plan; a private introduction rehearsal where recording is optional |
| Interview Ready | D3 step 3, D5 step 5 | the opening answer came before day 6 |
| | D6 step 3 | three parts in order; two pieces of work, one that went wrong; the thinking sentence |
| | D6 step 4 (VIDEO), step 5 | the quiz comes straight after the video and tests the example and the thinking sentence |
| | D6 steps 6, 7 | the call, the follow-up, the say-it-aloud option, the log |
| | Activity `IR_PHONE_HIRING_MANAGER` | the interviewer waits through silence and presses for specifics |
| The Speech Toolkit | D1 steps 2 to 6 | term "extra moves"; video; quiz; spoken questions with mirror or camera; awareness form |
| | D2 steps 3 to 9 | cue steps; two VIDEO steps; vowel activity, then consonant activity; trial log |
| | D4 steps 3, 5, 6 | choose a test before the video; three conversations; no length |
| | D5 steps 3 to 7 | chunking; example line; two tests; quiz; activity starts with the example line; trial log |
| | D7 | the extra moves day |
| | D8 | keep what earned a place; an empty kit is allowed |

## Term drift to watch

These rows hold today, but the video and the text use different words for the
same thing. A rewrite should not widen the gap. It may close it only by using
the video's word in the text, never by asking for a video change.

- Speech Toolkit D2: the videos say "easy onset" and "light contact". The text
  says "soft start" and "light touch", and never uses the video names.
- Art of Disclosure: the video says "three styles". Day 2 says "three shapes".
- Word Swap: the video says "a gentle repetition on purpose". Day 5 says
  "bounce".
- Speech Toolkit D1: the video says "the awareness form". The form's title on
  the day is "What you noticed, and what you already reach for".
- Speech Toolkit D1: Pip's example is a hand pressing into his leg. The form
  has no hand option, so the user would tick "Something else".

## Notes for maintainers

- `video-locked-terms.md`, "One known conflict", says the Speech Toolkit day 2
  video says "less press, not less contact". The live captions do not contain
  that phrase. It is in the day 2 text (step 3). The Light Contact video says
  "exploring less pressure while still forming the sound".
- `video-locked-terms.md` locks "three styles" for Art of Disclosure day 1.
  That phrase is only in the video. The program text says "shapes".
- `docs/programs/video-audit-2026-09-22/DETAILED-COMPARISON.md` says the
  iceberg drawing conflict is fixed. Day 1 is fixed. Day 2 step 1 still says
  the user drew an iceberg (see IB2).

---

## 1. The Whole Iceberg

Understanding Your Voice, day 1, step 1 (VIDEO). Video ID
`57b0ad65-bee1-4485-a1f2-970f97ec779d`.

**The video's own sequence.** Sheehan's iceberg. A listener hears a repeated
first sound and misses the rest. Today: two lists, what someone could notice
and what they would not see. An example pair. No drawing needed. A roadmap:
causes, variability, explanations, then effort, a swap, a card and a spoken
reply. Begin with one item on each list.

**Does the program repeat or depend on it?** Yes. Day 1 step 4 repeats the
task in its own words ("write two short lists ... You do not need to draw an
iceberg"). Step 3 gives its own roadmap ("Days 2 to 5 are the machinery. Day 6
is the deepest part of the iceberg. Day 7 is what actually helps"). Both
roadmaps must describe the same days.

- [ ] **IB1** `00:00:32,120` "Today, you will write two short lists." / `00:00:36,560` "First, what someone else could notice." / `00:00:40,340` "Second, what they would not see."
  - Direction: same-day.
  - Points to: D1 step 4, "write two short lists: what somebody could notice, and what they would not see." D1 step 6 drill "Your Own Iceberg": "Two lists ... Above the line: what somebody sitting opposite you would actually notice. Below the line: what they would not."
  - Must stay true: day 1 task is two written lists; the first is what others could notice, the second is what they would not see; that order.
  - Today: holds.
- [ ] **IB2** `00:00:50,260` "You do not need to draw an iceberg."
  - Direction: same-day.
  - Points to: D1 step 4, "You do not need to draw an iceberg."
  - Must stay true: no step on any day asks for, or says the user made, a drawing.
  - Today: **broken.** D2 step 1 (bridge in) says: "Yesterday you drew your own iceberg. Two lists, and the lower one is a list most people have never written down anywhere before."
- [ ] **IB3** `00:00:52,880` "That account gives you a starting point for learning about causes, why stuttering varies, and explanations you have heard."
  - Direction: forward.
  - Points to: D2 "You did not cause this" ("The timing circuit, and where it came from"); D3 "Why it comes and goes"; D4 "What you were told" ("The explanations you were handed").
  - Must stay true: causes, then variability, then other people's explanations, on days 2, 3 and 4 in that order.
  - Today: holds.
- [ ] **IB4** `00:01:02,100` "Later, you will notice effort before speaking."
  - Direction: forward.
  - Points to: nearest match is D5 step 6, drill "Where Your Bracing Sits": "Bring to mind a word you got stuck on recently. Then walk your attention through the speaking machinery ... where it tightened first and where it tightened hardest." D5 step 4 also says "For some people the bracing does not even wait for the word."
  - Must stay true: a later day has an exercise about noticing physical effort around speaking.
  - Today: **unclear.** The day 5 drill looks at a remembered stuck word, not at effort before speaking. No day asks the user to notice effort before they speak.
- [ ] **IB5** `00:01:06,700` "Look back at a word swap and put useful information into a card and a private spoken reply."
  - Direction: forward.
  - Points to: D6 step 6 drill "One Swap, Found": "Think back over the last few days and find one swap." D7 step 7 card (four lines, including "What you say to the next person who explains your speech to you"). D7 step 9 drill "Your Reply": "Say your reply out loud, twice." D7 step 8: "said out loud, on your own, twice."
  - Must stay true: day 6 looks back (not a live catch); day 7 has a card and a reply said out loud, alone.
  - Today: holds.
- [ ] **IB6** `00:01:14,760` "The two lists let you describe your speech and the experience around it together."
  - Direction: same-day.
  - Points to: D1 step 6 drill, both lists.
  - Must stay true: the lists cover speech (first list) and experience (second list).
  - Today: holds.
- [ ] **IB7** `00:01:27,520` "Begin with one thing people could notice and one thing they might miss."
  - Direction: same-day.
  - Points to: D1 step 6 drill; D1 step 4 "Before any of that, write two short lists".
  - Must stay true: the day's first task is the two lists.
  - Today: holds.

**Shared facts and examples (not rows).** "Psychologist and stuttering
researcher, Joseph Sheehan" (the text says "A researcher named Joseph
Sheehan"; the quiz calls him "a specific clinician"). The example pair "I
repeated the first sound, and I worried about their reaction".

## 2. The Art of Disclosure

The Art of Disclosure, day 1, step 1 (VIDEO). Video ID
`08464c80-3098-4df9-869b-94755ffd7644`.

**The video's own sequence.** A study of 338 viewers and three conditions.
The limits of a rating study. Two wordings compared. An optional request.
Today: one line. Tomorrow: three styles and a mirror, five times. Later: try
it, answer unwanted advice, decide where it goes. The final card includes
people who do not need to know. Start writing.

**Does the program repeat or depend on it?** Yes. D1 step 2 repeats the
study (338 listeners, informative, apologetic, none) and gives its own
roadmap: "You write the line today and say it alone tomorrow. Then somebody
who already knows, then a stranger, then the front of a real conversation, and
on day seven the first name on your list." The two roadmaps must agree.

- [ ] **A1** `00:00:44,600` "Today, you will write one line of your own."
  - Direction: same-day.
  - Points to: D1 step 5 activity "Write your sentence": "One sentence, your words." D1 step 6 form "Your line".
  - Must stay true: day 1 task is writing one line; nothing is said aloud today.
  - Today: holds.
- [ ] **A2** `00:00:47,320` "Tomorrow, you will explore three styles and try your line in a mirror five times."
  - Direction: forward.
  - Points to: D2 step 3, "There are three shapes that work" (passing mention, opener, light one). D2 step 5, "Say your line, the one you wrote yesterday, out loud five times."
  - Must stay true: day 2 has exactly three ways of saying it; a mirror; five repetitions; it is day 2.
  - Today: holds. Term drift: the text says "shapes".
- [ ] **A3** `00:00:52,600` "Later conversations give you chances to try it, respond to unwanted advice, and decide where the line belongs."
  - Direction: forward.
  - Points to: D3 "Say it to someone who already knows"; D4 "Tell one stranger"; D5 "When the reply is clumsy" ("A small number of people answer with something like: 'Have you tried slowing down?'"); D6 "Open with it" ("Where the line sits in the conversation").
  - Must stay true: real-person practice after day 2; one day on replies to advice; one day on where in a conversation the line goes; advice before position.
  - Today: holds.
- [ ] **A4** `00:01:04,240` "The final card includes people who do not need to know."
  - Direction: forward.
  - Points to: D7 step 7 card: "your three names marked told, planned or no need". Form field: "The people you named at the start. Mark each one: told, planned, or no need."
  - Must stay true: the day 7 card lets a person be marked as not needing to know.
  - Today: holds.
- [ ] **A5** `00:01:07,720` "Start by writing a sentence that explains your speech in words you would use, without asking you to apologise for it."
  - Direction: same-day.
  - Points to: D1 step 5, "Use the word you actually use, stammer or stutter. Say what they might notice, and leave any apology out of it."
  - Must stay true: own words; no apology.
  - Today: holds.

**Shared facts and examples (not rows).** "338 viewers", three conditions,
informative rated better than no disclosure (D1 step 2 says "338 listeners"
and "moved six of them"). The example "I stutter, so you may hear me pause or
repeat a sound." The optional request "Please give me time to finish." Added
to the example line it makes 18 words; D2 step 3 check 3 says "Keep it under
about fifteen words". Do not make that check stricter.

## 3. The Word Swap

The Word Swap, day 1, step 1 (VIDEO). Video ID
`4632ca44-3992-4bda-b37d-e1ee27689bda`.

**The video's own sequence.** "Movies" and "cinema". Today: two lists, what
people believe and what keeping that picture takes. An example pair. Private
and written. Tomorrow: notice without changing. Later: an original word, an
unplanned exchange, a repetition on purpose. A swap can be kept, and the card
has room for it. Begin with the lists.

**Does the program repeat or depend on it?** Yes. D7 step 3 lists the week
day by day ("Day two you watched ... Day three you ... said the word ... Day
four you went into one exchange with no run-up ... Day five you put a bounce
on a word"). That list and the video's roadmap must match.

- [ ] **W1** `00:00:36,040` "Today, you'll write two short lists." / `00:00:39,660` "What people around you believe about your speech and what keeping that picture takes."
  - Direction: same-day.
  - Points to: D1 step 6 activity: "Write down two things. One: what the people around you believe about how you speak ... Two: what keeping that picture true takes."
  - Must stay true: two lists; belief first, cost second; the phrase "keeping that picture".
  - Today: holds.
- [ ] **W2** `00:00:58,700` "These lists give you something specific to look back at."
  - Direction: forward.
  - Points to: D2 step 1, "Yesterday you wrote two lists"; D7 step 3, "Day one you priced it"; D7 step 6 week review of the logs.
  - Must stay true: a later day refers back to the day 1 lists.
  - Today: holds.
- [ ] **W3** `00:01:02,340` "Today's task is private and written."
  - Direction: same-day.
  - Points to: D1 step 6, "Nothing here is spoken out loud." and "Nothing here is spoken and nobody else reads it."
  - Must stay true: day 1 has no spoken task and no other person.
  - Today: holds.
- [ ] **W4** `00:01:06,900` "Tomorrow, you'll notice a swap without trying to change it."
  - Direction: forward.
  - Points to: D2 step 5 "Watch one day of it": "Change none of it."
  - Must stay true: day 2 is observe only.
  - Today: holds.
- [ ] **W5** `00:01:11,820` "Later, you can explore an original word, an unplanned exchange, and a gentle repetition on purpose."
  - Direction: forward.
  - Points to: D3 "One word" ("say the word you meant instead"); D4 "One exchange, unplanned"; D5 "One bounce, on purpose".
  - Must stay true: these three tasks, in this order, after day 2; the repetition is light and chosen.
  - Today: holds. Term drift: the text says "bounce".
- [ ] **W6** `00:01:21,300` "A swap can still be a choice you want to keep."
  - Direction: forward.
  - Points to: D6 step 3, "You are allowed to swap ... Not as a slip. As a decision."
  - Must stay true: the program never requires the user to stop swapping.
  - Today: holds.
- [ ] **W7** `00:01:25,000` "Your final word card has room for that."
  - Direction: forward.
  - Points to: D7 step 7 card: "the ones you are keeping on purpose".
  - Must stay true: the day 7 card has a line for swaps kept on purpose.
  - Today: holds.
- [ ] **W8** `00:01:36,040` "Begin with your two lists."
  - Direction: same-day.
  - Points to: D1 step 6.
  - Must stay true: the lists are day 1's task.
  - Today: holds.
- [ ] **W9** `00:01:38,180` "They give you a place to start before changing a single word."
  - Direction: forward.
  - Points to: D2 (change nothing), then D3 (first word said).
  - Must stay true: no day before day 3 asks the user to change a word.
  - Today: holds.

**Shared facts and examples (not rows).** "movies" and "cinema". "my
colleagues think I rarely stutter and I change words before calls."

## 4. Bouncing Back

Bouncing Back (The Post-Block Reset), day 1, step 1 (VIDEO). Video ID
`9e38749b-e5fc-46e1-90c8-f109a72b0132`.

**The video's own sequence.** After a hard call, Pip goes over one word. The
rest of that day (sleep, rushing, a noisy corridor). Today: list the context
of one hard day. Four prompt questions. The hour-before option. Later: plain
account, friend version, one review with an end. Starter phrase.

**Does the program repeat or depend on it?** Yes. The D1 step 7 activity
repeats the task and prompts. D7 step 3 lists the six days in order and must
keep days 3, 5 and 6 in the same order as the video.

- [ ] **B1** `00:00:39,660` "That's where bouncing back begins, with the context around one hard speaking day."
  - Direction: same-day.
  - Points to: D1 step 7 "What else was true that day".
  - Must stay true: day 1 task is the context of one hard day.
  - Today: holds.
- [ ] **B2** `00:00:46,140` "In today's writing exercise, you can choose a day from the last two weeks, and note what else was true."
  - Direction: same-day.
  - Points to: D1 step 7, "Pick one hard speaking day from the last two weeks and write down everything else that was true about it."
  - Must stay true: written; "last two weeks"; "what else was true".
  - Today: holds.
- [ ] **B3** `00:00:53,140` "How had you slept?" / `00:00:54,760` "Who was there?" / `00:00:56,080` "Were you rushed?" / `00:00:57,540` "What were you already concerned about?"
  - Direction: same-day.
  - Points to: D1 step 7, "How you slept, what you were dreading, who was there, whether you had eaten, how rushed you were."
  - Must stay true: sleep, who was there, rushing and worries all stay among the prompts.
  - Today: holds.
- [ ] **B4** `00:01:00,320` "You can focus on just the hour before the moment if that feels more manageable."
  - Direction: same-day.
  - Points to: D1 step 7, "Three ways to do it: the whole day, the hour before the moment, or the week around it."
  - Must stay true: "the hour before the moment" stays an option.
  - Today: holds.
- [ ] **B5** `00:01:05,480` "Later in the week, you'll practice writing a plain account, finding words you would use with a friend, and giving one review a clear ending."
  - Direction: forward.
  - Points to: D3 "What actually happened" ("Say what happened, in the plainest words you have"); D5 "What you would say to a friend"; D6 "One review, with an end on it".
  - Must stay true: these three tasks exist, in this order, after day 1.
  - Today: holds.
- [ ] **B6** `00:01:14,200` "For today, a short list gives you more of the day to work with."
  - Direction: same-day.
  - Points to: D1 step 7.
  - Must stay true: the day 1 output is a list.
  - Today: holds.
- [ ] **B7** `00:01:19,080` "Start with: “That day, I had also…”"
  - Direction: same-day.
  - Points to: D1 step 7 placeholder, "That day I had also..."
  - Must stay true: the placeholder keeps these words.
  - Today: holds.

**Shared facts and examples (not rows).** Pip slept poorly, was rushing, took
the call in a noisy corridor. "Those details don't tell us why he stuttered."

## 5. Whose Advice Are You Following

Dating, Intimacy & Vulnerability, day 1, step 1 (VIDEO). Video ID
`b6c94cdb-f70d-450d-b0c3-4bae767ef538`.

**The video's own sequence.** Two opposite pieces of advice. You decide.
Private writing: one piece of advice, its words, who said it, whether you
agreed, what following it took. An example. Later: timing, an optional line,
rejection, interruptions. The week ends with a plan and a private
introduction. Recording and disclosure stay optional. No date to arrange.
Start with one line.

**Does the program repeat or depend on it?** Yes. D1 step 4 lists the advice,
including both opposite lines, and the D1 step 6 drill asks for the same four
things. D7 step 4 ("What you have now") recaps the week.

- [ ] **D1** `00:00:03,200` "When it comes to dating and stuttering, you might hear two opposite pieces of advice." (followed by "Tell them straight away." and "Don't mention it.")
  - Direction: same-day.
  - Points to: D1 step 4 list, "Do not mention it, you will only draw attention to it." and "Definitely mention it, get it out of the way." Then: "Notice that several of those contradict each other".
  - Must stay true: both opposite lines stay on the day 1 list.
  - Today: holds.
- [ ] **D2** `00:00:14,880` "Both can sound certain, but you are the one deciding what to say and when."
  - Direction: forward.
  - Points to: D3 step 3, "choosing not to mention it is not avoidance. It is a decision about who gets access to what, and it is yours." D1 step 2, "The timing stays yours".
  - Must stay true: no day tells the user when or whether to disclose.
  - Today: holds.
- [ ] **D3** `00:00:21,750` "This week begins with private writing."
  - Direction: same-day.
  - Points to: D1 step 6 drill and step 7 form. D1 step 3, "Everything you write here stays with you."
  - Must stay true: the first task is written and private.
  - Today: holds.
- [ ] **D4** `00:00:25,060` "Pick one piece of advice you have heard." / `00:00:28,760` "Write the words, who said them, whether you agreed, and what following them took, if anything."
  - Direction: same-day.
  - Points to: D1 step 6 drill "Advice You Never Agreed To": "Write it out in the words it was actually said in. Then answer two things about it: who said it, and whether you ever agreed with it. Last, write what following it has cost you, if anything."
  - Must stay true: one piece of advice; the four parts (words, who, agreed, cost).
  - Today: holds.
- [ ] **D5** `00:00:53,340` "Writing it down gives you a specific rule to examine." / `00:00:57,380` "Did you agree to it?" / `00:00:59,040` "Or did you start following it because someone sounded sure?"
  - Direction: same-day.
  - Points to: D1 step 4, "a rule you follow without having agreed to it is the expensive kind".
  - Must stay true: the day frames advice as a rule you may never have agreed to.
  - Today: holds.
- [ ] **D6** `00:01:03,500` "Later you'll consider timing."
  - Direction: forward.
  - Points to: D2 step 4, "Where it usually goes, if it goes anywhere" (five moments).
  - Must stay true: a later day covers when a line could go.
  - Today: holds.
- [ ] **D7** `00:01:05,740` "An optional line about your speech, worries about rejection and replies to interruptions."
  - Direction: forward.
  - Points to: D3 "Say it your way, or not at all"; D4 "The rejection you're picturing"; D6 "When they finish it for you".
  - Must stay true: the line stays optional; rejection before interruptions; all three after day 2.
  - Today: holds.
- [ ] **D8** `00:01:12,720` "The week ends with a relationship plan and a private introduction you can rehearse."
  - Direction: forward.
  - Points to: D7 step 8 form "Your plan, including not yet"; D7 step 11 activity "Tell me about yourself": "Nobody is on the other end of this".
  - Must stay true: day 7 has a plan and a solo rehearsal of an introduction.
  - Today: holds.
- [ ] **D9** `00:01:19,280` "Recording and disclosure remain your choice."
  - Direction: forward.
  - Points to: D7 step 11, "Point your phone at yourself and record, or do it without recording if you would rather ... Put your line about stuttering in if you want it there, and leave it out if you do not".
  - Must stay true: no step requires a recording or a disclosure.
  - Today: holds.
- [ ] **D10** `00:01:28,720` "There is no date to arrange before you begin."
  - Direction: same-day.
  - Points to: D1 step 2, "There is no date to go on and nothing here carries a deadline." D1 step 3, "Nothing here sends you at anybody."
  - Must stay true: no day in the program sends the user on a date or to message anybody.
  - Today: holds.
- [ ] **D11** `00:01:32,920` "Start with one line you have heard." / `00:01:36,020` "Write whether it was ever a rule you agreed to follow."
  - Direction: same-day.
  - Points to: D1 step 6 drill.
  - Must stay true: the drill asks whether the user agreed.
  - Today: holds.

**Shared facts and examples (not rows).** The example account "tell them
straight away. A friend said it. I wasn't ready." The line "You can decide
which advice to keep, change, or leave behind" has no matching step; it is a
general statement and needs nothing.

## 6. Give an Answer They Can Follow Up

Interview Ready, day 6, step 4 (VIDEO). Video ID
`b94dcede-3d14-4f8e-808e-f4796cdfcb2e`.

**The video's own sequence.** Recap of the opening answer. "You've just read
the three parts." Three strategies: match examples to the role (job
description), STAR, practise the follow-up. Two pieces of work, one that went
wrong. STAR mapped onto the lesson's three parts. Pip's example (client wants
two weeks, team estimates six, two releases). Numbers. A follow-up question
and his answer. Questions to practise aloud. The thinking sentence. Then:
quiz, notes, call, the say-it-aloud option, log.

**Does the program repeat or depend on it?** Partly. D6 step 3 teaches the
three parts, the thinking sentence and the two pieces of work, and comes
before the video. The text does not teach STAR or matching to the job
description; those live only in the video. D7 step 2 recall
(`ir_d6_r1` to `ir_d6_r4`) depends on day 6 content: the "went wrong"
example, the pressure being about what you have done, and the thinking
sentence.

- [ ] **IR1** `00:00:03,200` "The opening answer introduced you."
  - Direction: backward.
  - Points to: D3 step 3, "An opening answer that works has three parts"; D5 step 5, "Record ninety seconds of your opening answer"; D6 step 1, "your opening answer".
  - Must stay true: the "opening answer" is taught before day 6, under that name.
  - Today: holds.
- [ ] **IR2** `00:00:06,188` "Today’s hiring manager wants to know what you’ve actually done."
  - Direction: same-day.
  - Points to: D6 title "The hiring manager"; D6 step 3, "Give a general answer and you will be asked for a real one."
  - Must stay true: day 6 is the hiring manager; the pressure is about substance.
  - Today: holds.
- [ ] **IR3** `00:00:10,085` "You’ve just read the three parts of a concrete example."
  - Direction: backward.
  - Points to: D6 step 3, "What makes an answer concrete. Three pieces, in order."
  - Must stay true: the TEXT step with the three parts comes directly before the VIDEO step; there are exactly three parts.
  - Today: holds.
- [ ] **IR4** `00:00:13,775` "Now let’s put them to work, including the question that comes next: “Can you tell me more about what you did?”"
  - Direction: forward.
  - Points to: D6 step 6 call. Call script: "press gently for specifics. If they give a vague answer, ask 'can you give me a concrete example?'"
  - Must stay true: the call asks at least one follow-up about what the user did.
  - Today: holds. The script's wording differs from the caption; keep the follow-up about the user's own actions.
- [ ] **IR5** `00:00:37,612` "First, start with the job description." / `00:00:41,188` "Pick two requirements you could demonstrate with real experience." / `00:00:44,870` "Beside each, note a specific occasion when you used that skill."
  - Direction: same-day.
  - Points to: no step. D1 step 5 intake collects company and role only ("the interviewer says your company and your role out loud").
  - Must stay true: the user can reach a job description or list of requirements.
  - Today: **unclear.** No day mentions a job description or asks the user to have one. D6 step 3 does not teach matching examples to the role. The only mention is a wrong quiz option in `ir_d6_c1`: "A list of the skills the job advert asked for."
- [ ] **IR6** `00:01:02,130` "Choose two pieces of work for today." / `00:01:05,025` "Make one a time something went wrong and you dealt with it."
  - Direction: same-day.
  - Points to: D6 step 3, "Pick two pieces of work before you start ... Make one of the two a thing that went wrong and got fixed." D7 recall `ir_d6_r1`.
  - Must stay true: two pieces; one about something that went wrong.
  - Today: holds.
- [ ] **IR7** `00:01:45,867` "This fits the three parts in this lesson: the situation, including your responsibility; what you did; and what happened."
  - Direction: same-day.
  - Points to: D6 step 3, "1. The situation ... 2. What you did ... 3. What happened."
  - Must stay true: the three parts, their names and their order.
  - Today: holds.
- [ ] **IR8** `00:03:57,486` "If you need a moment to choose an example, you can say, “Let me think about that for a second.”"
  - Direction: same-day.
  - Points to: D6 step 3, "The sentence that buys you time: 'Let me think about that for a second.'" Quiz `ir_d6_c2`. D7 recall `ir_d6_r3`.
  - Must stay true: the exact sentence.
  - Today: holds.
- [ ] **IR9** `00:04:08,455` "Today’s practice interviewer waits and responds to the content."
  - Direction: same-day.
  - Points to: `IR_PHONE_HIRING_MANAGER` call script, "Give them room to think; a silence is fine and you should let it sit." D1 step 1, "Pauses, repeats, restarts and blocks go completely unremarked".
  - Must stay true: the day 6 interviewer waits through silence and never comments on speech.
  - Today: holds.
- [ ] **IR10** `00:04:13,275` "Nothing here asks you to speak faster or hide a stutter."
  - Direction: same-day.
  - Points to: D1 step 1 ("None of them ever comments on how you speak"); recall `ir_d5_r4` ("How it sounded").
  - Must stay true: no day 6 step asks for speed or concealment.
  - Today: holds.
- [ ] **IR11** `00:04:19,042` "Next comes a short quiz on the example and the thinking-time sentence."
  - Direction: forward.
  - Points to: D6 step 5 quiz, `ir_d6_c1` (what makes an answer concrete) and `ir_d6_c2` (the thinking sentence).
  - Must stay true: the QUIZ step comes straight after the VIDEO; it is short; it covers these two topics.
  - Today: holds.
- [ ] **IR12** `00:04:25,168` "Then, before your practice call, choose your two examples and make brief notes: the situation, what you did, and what happened." / `00:04:35,240` "Note what you expect the manager to ask."
  - Direction: forward.
  - Points to: D6 step 6, "Pick your two examples first ... Say what you think will happen before you start." D6 step 7, "what you expected the manager to do with a general answer".
  - Must stay true: choose examples before the call; write an expectation before the call.
  - Today: holds. The notes are the user's own; no field holds them.
- [ ] **IR13** `00:04:38,587` "Then take the call and let the follow-up come."
  - Direction: forward.
  - Points to: D6 step 6, "Let the follow-up come rather than heading it off".
  - Must stay true: day 6 has a call with a follow-up.
  - Today: holds.
- [ ] **IR14** `00:04:42,363` "If you’d rather not call today, you can say your answers aloud instead."
  - Direction: same-day.
  - Points to: D6 step 6, "If you would rather not call today, say your answers out loud instead, standing up".
  - Must stay true: the say-aloud alternative stays.
  - Today: holds.
- [ ] **IR15** `00:04:47,970` "Afterwards, record what actually happened and one detail you want to keep."
  - Direction: forward.
  - Points to: D6 step 7 log, "what they actually did with it. One line to keep at the end."
  - Must stay true: a log after the call with what happened and one line to keep.
  - Today: holds.

**Shared facts and examples (not rows).** STAR (situation, task, action,
result). Pip's example: the client wanted it in two weeks, the team
estimated six, two releases. The D6 text example uses "six weeks" as the
first phase ("what we could ship in six weeks and what would come later").
Keep the two examples separate; do not merge their numbers. "Use a number when
you know it" matches the text's "with a number in it if there is one".

## 7. Notice the Movement Before You Change It

The Speech Toolkit, day 1, step 3 (VIDEO). Video ID
`ebdccad3-85c2-42f5-909d-ed11a2bc9693`.

**The video's own sequence.** Pip's hand presses into his leg. The lesson's
term "extra moves". What a movement can mean. Pip's two observations and his
note. Today: observe only. Change comes later. After the check: questions
aloud, mirror or camera, the awareness form. Day seven returns to it.

**Does the program repeat or depend on it?** Yes. D1 step 2 defines "extra
move" and says "Day seven comes back to them." D7 step 3 says "You listed
your own on day one". D8 recall `st_d7_r2` says the list came from "The
inventory you filled in on day one."

- [ ] **NM1** `00:00:13,550` "This lesson calls movements like that extra moves."
  - Direction: same-day.
  - Points to: D1 step 2, "An extra move is the thing that rides along with a hard word: a blink, a head nod, a tap on the leg, filler words, eyes leaving the person you are talking to."
  - Must stay true: the term "extra moves" is defined on day 1, before the video.
  - Today: holds.
- [ ] **NM2** `00:00:57,469` "That is enough to notice today." / `00:01:15,075` "Today’s job is to observe."
  - Direction: same-day.
  - Points to: D1 step 2, "Today you are not trying anything. You are looking." D1 step 8, "the only day this week with no tool in it."
  - Must stay true: day 1 has no tool and no change.
  - Today: holds.
- [ ] **NM3** `00:01:18,294` "There is no target for keeping your body still, holding eye contact, or making your speech sound different."
  - Direction: same-day.
  - Points to: D1 step 1, "No day grades the sound of it"; D1 step 5, "Nothing is scored and nothing is counted."
  - Must stay true: day 1 sets no stillness, eye-contact or sound target.
  - Today: holds.
- [ ] **NM4** `00:01:25,420` "Changing a movement belongs to a later lesson, when you can explore what that changes for you."
  - Direction: forward.
  - Points to: D7 "The extra moves you don't need", step 5 "Hold one extra move still".
  - Must stay true: a later day is where a movement is changed.
  - Today: holds.
- [ ] **NM5** `00:01:32,165` "After the short check, the activity gives you questions to answer aloud."
  - Direction: forward.
  - Points to: D1 step 4 quiz (three questions), then D1 step 5 activity: "Answer each question out loud". The activity (`TECH_COGNITIVE_MIRROR_WORK_GENERAL`) supplies spoken prompts.
  - Must stay true: QUIZ directly after the VIDEO, then an activity with questions answered aloud.
  - Today: holds.
- [ ] **NM6** `00:01:36,823` "If you’d like to try it, watch your face and shoulders in a mirror or on camera."
  - Direction: same-day.
  - Points to: D1 step 5, "watch what your face and shoulders do ... camera on and watching, camera on with the screen turned away, or a bathroom mirror".
  - Must stay true: face and shoulders; mirror or camera both allowed.
  - Today: holds.
- [ ] **NM7** `00:01:52,461` "Then use the awareness form to record what you recognise."
  - Direction: forward.
  - Points to: D1 step 6 form `activity.awareness_inventory`: "Tick what you recognise".
  - Must stay true: a form after the activity where the user ticks what they recognise.
  - Today: holds. Term drift: the step's title is "What you noticed, and what you already reach for". The form has no hand option for Pip's example; "Something else" is the only fit.
- [ ] **NM8** `00:01:57,344` "The program returns to extra moves on day seven."
  - Direction: forward.
  - Points to: D7 "The extra moves you don't need"; D1 step 2, "Day seven comes back to them."
  - Must stay true: the extra moves day is day 7.
  - Today: holds.
- [ ] **NM9** `00:02:01,153` "For today, the useful result is a clear observation: what happened, and what you noticed about the effort."
  - Direction: same-day.
  - Points to: D1 step 5 prompt, "What did your face or shoulders do that you had not noticed before?"
  - Must stay true: the day 1 output is an observation.
  - Today: holds.

**Shared facts and examples (not rows).** "a firm blink, a head movement, or a
hand tightening". The form lists "Blinking hard" and "Moving my head or jaw";
it has no hand option. Pip's shoulders feel tight; the form's tension list
includes "Shoulders".

## 8. Easy Onset

The Speech Toolkit, day 2, step 5 (VIDEO). Video ID
`14e1aa33-5d3a-4a3f-9b69-e8c3da4cfc7b`.

**The video's own sequence.** What to listen for. A breathy cue. "after" with
a longer cue, then a shorter cue. The H is temporary. A phrase, "open it".
Make the cue smaller, then leave it out. Notice effort. Judge it for the kit.

**Does the program repeat or depend on it?** Yes. D2 step 3 and the step 7
activity use the same three stages ("hhh-apple ... h-apple ... apple"). The
step 7 word list includes "after" and "open".

- [ ] **EO1** `00:00:03,499` "What are you listening for in easy onset?" / `00:00:09,879` "Easy onset means starting your voice gradually."
  - Direction: same-day.
  - Points to: D2 step 3 "A soft start": "let a little air move before the sound arrives". D2 step 7 "Try the soft start, once".
  - Must stay true: day 2 teaches a gradual voice start on vowel words.
  - Today: holds. Term drift: the text never says "easy onset".
- [ ] **EO2** `00:00:20,979` "First, with a longer cue." / `00:00:32,329` "Now listen with a shorter cue." / `00:01:11,930` "Explore making the cue smaller, then leaving it out while keeping a gradual voice start."
  - Direction: same-day.
  - Points to: D2 step 3, "1. Say hhh-apple ... 2. Say h-apple, with the h much shorter. 3. Say apple, with no h at all". D2 step 7, same three stages.
  - Must stay true: three stages, long cue, short cue, no cue, in that order.
  - Today: holds.
- [ ] **EO3** `00:00:43,220` "The extra H sound is a temporary practice cue." / `00:00:47,139` "It is not part of the word."
  - Direction: same-day.
  - Points to: D2 step 3, "The h is only how you find that feeling; it is not meant to stay in the word." D2 step 7, "the h is not meant to stay in the word."
  - Must stay true: the H does not stay in the word.
  - Today: holds.
- [ ] **EO4** `00:01:21,970` "Notice the effort and attention it takes."
  - Direction: same-day.
  - Points to: D2 step 3 test "Did that take less effort than usual?" and "What did it cost?"; D2 step 9 log cost line, "Attention, effort, anything you stopped doing."
  - Must stay true: effort and cost are what the user judges.
  - Today: holds.
- [ ] **EO5** `00:01:25,029` "That gives you something useful to judge: whether this is an option you want in your kit."
  - Direction: forward.
  - Points to: D2 step 9 log, "whether you are keeping it"; D8 "Your kit".
  - Must stay true: the word "kit"; keeping is a choice.
  - Today: holds.

**Shared facts and examples (not rows).** The words "after" and "open it".
Both "after" and "open" are in the step 7 list.

## 9. Light Contact

The Speech Toolkit, day 2, step 6 (VIDEO). Video ID
`3ee406c1-8f69-4904-a5bb-1370b03f2f04`.

**The video's own sequence.** Lips still close. "paper": lips meet and
release. Less pressure while still forming the sound. "tumble": tongue
behind the upper front teeth. Choose what to notice. Try "paper" once. Easy
onset and light contact side by side. Next: vowel words, then consonants.
Judge each. The kit can take either, both or neither.

**Does the program repeat or depend on it?** Yes. D2 step 3 "A light touch"
and the step 8 activity teach the same idea ("Less press, not less contact")
on baby, puppy, table. Both videos sit between the quiz (step 4) and the two
activities (steps 7 and 8).

- [ ] **LC1** `00:00:14,820` "Light contact means exploring less pressure while still forming the sound."
  - Direction: same-day.
  - Points to: D2 step 3, "They have to close ... What you can change is how hard they press and how long they stay shut ... Less press, not less contact."
  - Must stay true: lips or tongue still close; only the pressure changes.
  - Today: holds. Term drift: the text says "light touch".
- [ ] **LC2** `00:01:01,299` "Before you try, choose what to notice: the effort, or how easily you can stay with the word."
  - Direction: same-day.
  - Points to: D2 step 3 tests, "Did that take less effort than usual?" and "Could I still say the word I meant". D2 step 7, "Pick the test this one has to pass before you begin". D2 step 8, "Same test as the one you picked a moment ago".
  - Must stay true: the test is chosen before trying; these two options.
  - Today: holds.
- [ ] **LC3** `00:01:23,519` "Easy onset explores how the voice begins." / `00:01:27,799` "Light contact explores the pressure at a consonant."
  - Direction: same-day.
  - Points to: D2 step 3, "A soft start" (vowel words) and "A light touch" (p, b, t, d, k, g).
  - Must stay true: one tool for vowel starts, one for consonant pressure.
  - Today: holds. Term drift as in EO1 and LC1.
- [ ] **LC4** `00:01:32,239` "Next, you’ll try the vowel words, then the consonants."
  - Direction: forward.
  - Points to: D2 step 7 (ten vowel words), then D2 step 8 (baby, puppy, table).
  - Must stay true: both VIDEO steps come before both activities; vowel activity before consonant activity.
  - Today: holds.
- [ ] **LC5** `00:01:36,559` "Use your notes to judge each."
  - Direction: forward.
  - Points to: D2 step 9 log: "Today held two tools, so answer for the one you would take further and use the cost line to say if the other went differently."
  - Must stay true: the user can judge each tool.
  - Today: **unclear.** Each activity has its own note prompt, but the one log judges one tool and leaves the other to the cost line.
- [ ] **LC6** `00:01:39,239` "Your kit can include either, both, or neither."
  - Direction: forward.
  - Points to: D2 step 9, "Not keeping either is one of the answers offered." D1 step 1, "Finishing with an empty kit is a finished answer". D8 step 3.
  - Must stay true: keeping none stays a valid answer.
  - Today: holds.

**Shared facts and examples (not rows).** "paper" and "tumble" (the drill uses
baby, puppy, table). The recording also eases into the voice and lengthens
the vowel.

## 10. The Pause Is Yours

The Speech Toolkit, day 4, step 5 (VIDEO). Video ID
`fcec6db2-ceed-4bda-8524-44fe5e6f65ce`.

**The video's own sequence.** Research on answer timing in 10 languages. A
demonstration question and answer with a pause. What to notice. The research
describes conversations; the trial is yours. No count or length. Try it here,
then in three conversations. Use the test you chose. Tomorrow: breaks inside
sentences.

**Does the program repeat or depend on it?** Yes. D4 step 3 ("Today") says
the same task and tells the user to choose a test "Before the video". The
step 6 activity repeats the three conversations. D5 step 3 depends on day 4
("The break is a pause, which is why yesterday came first").

- [ ] **P1** `00:00:16,220` "This exercise gives you room to try a different pace."
  - Direction: same-day.
  - Points to: D4 step 6 activity.
  - Must stay true: the exercise changes when an answer starts. It must never become a rule about speaking rate (D4 step 3: "nothing in this week has a view on how fast you talk").
  - Today: holds.
- [ ] **P2** `00:00:36,260` "When you try it, notice whether that space feels useful, takes extra thinking, or changes very little."
  - Direction: same-day.
  - Points to: D4 step 6, "Say what you noticed in the moment before you started talking." D4 step 7 log.
  - Must stay true: the user reports what they noticed, and "no change" is an allowed result.
  - Today: holds.
- [ ] **P3** `00:00:48,220` "Your trial asks what the experience is like for you."
  - Direction: same-day.
  - Points to: D4 step 6, "Whether anybody else was bothered is not what you are testing"; D4 step 7 trial log.
  - Must stay true: the trial is about the user's experience, not the listener.
  - Today: holds.
- [ ] **P4** `00:00:52,560` "Today, there is no count or length to hit."
  - Direction: same-day.
  - Points to: D4 step 3, "It is not a count to keep." D4 step 6, "There is no technique in it and no length to hit."
  - Must stay true: no pause length or count target (three conversations is a task size, not a pause count).
  - Today: holds.
- [ ] **P5** `00:00:56,900` "Try it here."
  - Direction: same-day.
  - Points to: D4 step 6, "In the app first. The move is one beat of silence between the question arriving and your answer starting."
  - Must stay true: there is something in the app to try the pause on.
  - Today: **unclear.** The activity is a real-life challenge. It has no question in the app to pause before; the only question is the one in the video.
- [ ] **P6** `00:00:57,860` "Then let a beat pass before answering in three conversations that were happening anyway."
  - Direction: forward.
  - Points to: D4 step 6, "In three conversations that were happening anyway, let a beat pass before you answer a question".
  - Must stay true: three conversations; ones that were happening anyway; the word "beat".
  - Today: holds.
- [ ] **P7** `00:01:04,760` "Use the test you chose earlier and note any extra attention."
  - Direction: backward.
  - Points to: D4 step 3, "Before the video, choose one test for today ... Write down your choice and what you expect. Use that same test after the trial." D4 step 7 log cost line.
  - Must stay true: the test choice sits in a step before the VIDEO step.
  - Today: holds.
- [ ] **P8** `00:01:09,940` "Tomorrow adds breaks within longer sentences."
  - Direction: forward.
  - Points to: D5 "One chunk at a time".
  - Must stay true: chunking is day 5.
  - Today: holds.
- [ ] **P9** `00:01:14,150` "Start with the next question."
  - Direction: forward.
  - Points to: D4 step 6, "the next three questions anybody asks you".
  - Must stay true: the next question someone asks stays a valid way to start.
  - Today: holds.

**Shared facts and examples (not rows).** "yes or no exchanges in 10
languages" (Stivers and colleagues, 2009, per the audit). The program text
does not cite it; if a rewrite adds timing research, it must agree. The
demonstration: "Did you go out at the weekend?" "Yes, I went for a walk."

## 11. Keep the Meaning in the Sentence

The Speech Toolkit, day 5, step 4 (VIDEO). Video ID
`30b4ec4f-03d2-4a4d-8b89-1326f64ff670`.

**The video's own sequence.** Pip loses a paragraph's meaning. Yesterday's
pause. Chunking, groups of three or four words. The example line. Choose one
of two tests and write an expectation. Pip's result: easier, but meaning
lost. A short trial with three outcomes. Cost if it feels compulsory. After
the check: the example line, a paragraph read once alone, the trial log.

**Does the program repeat or depend on it?** Yes. D5 step 3 teaches chunking,
the same example line, the same two tests and the same "easier but lost the
meaning" case. The step 6 activity starts with the example line. D6 recall
`st_d5_r4` tests the same two-part judgment.

- [ ] **KM1** `00:00:20,030` "Yesterday, you explored a pause before an answer."
  - Direction: backward.
  - Points to: D4 "The pause is yours"; D5 step 1, "Yesterday you let one beat of silence stand before your answer".
  - Must stay true: the pause day is day 4.
  - Today: holds.
- [ ] **KM2** `00:00:23,310` "Today, the pauses sit inside a sentence."
  - Direction: same-day.
  - Points to: D5 step 3, "Chunking breaks one into short pieces with a small pause at each break."
  - Must stay true: day 5 is pauses inside a sentence.
  - Today: holds.
- [ ] **KM3** `00:00:27,410` "Chunking means breaking the sentence into short groups, with a small stop between them."
  - Direction: same-day.
  - Points to: D5 step 3 and step 6.
  - Must stay true: the term "chunking"; small stops.
  - Today: holds.
- [ ] **KM4** `00:00:33,281` "The activity uses groups of three or four words."
  - Direction: same-day.
  - Points to: D5 step 6, "pieces of three or four words".
  - Must stay true: three or four words.
  - Today: holds.
- [ ] **KM5** `00:00:41,170` "I am going to the store to buy some bread." (read in three groups)
  - Direction: same-day.
  - Points to: D5 step 3, "I am going / to the store / to buy some bread." D5 step 6, same line.
  - Must stay true: the exact line and its three breaks.
  - Today: holds.
- [ ] **KM6** `00:00:56,750` "This short exercise lets you hear and feel what the breaks do before deciding whether you want to use them."
  - Direction: same-day.
  - Points to: D5 step 6, "you can hear what the breaks do to a sentence before you decide whether to use them anywhere."
  - Must stay true: the activity is a short trial before any decision.
  - Today: holds.
- [ ] **KM7** `00:01:05,370` "Before your reading, choose one test." / `00:01:08,770` "Did it take less effort?" / `00:01:10,790` "Or, could I still follow what I was reading?"
  - Direction: same-day.
  - Points to: D5 step 3, "Before you read, pick one test. Did it take less effort than usual? Could I still follow what I was reading?" D5 step 6, same.
  - Must stay true: one test, chosen before reading; exactly these two.
  - Today: holds.
- [ ] **KM8** `00:01:14,510` "Pick the one you want to check, and jot down what you expect."
  - Direction: same-day.
  - Points to: D5 step 3, "Write down what you expect." D5 step 7 log, "Before you tried it, what did you expect?"
  - Must stay true: an expectation is written first.
  - Today: holds.
- [ ] **KM9** `00:01:23,427` "Suppose Pip chose following the meaning." to `00:01:38,850` "Both parts belong in the note."
  - Direction: same-day.
  - Points to: D5 step 3, "The reading can feel easier while you lose the meaning. If following the meaning was your chosen test, it did not pass. Record both results."
  - Must stay true: easier reading can still fail the meaning test; both results are recorded.
  - Today: holds.
- [ ] **KM10** `00:01:41,970` "This pattern belongs to a short trial." / `00:01:44,950` "You can choose it for a particular situation, leave it out, or remain undecided."
  - Direction: same-day.
  - Points to: D5 step 7 log options "Keeping it for one situation only", "Not keeping it", "Undecided, want another go".
  - Must stay true: those three answers stay on the log.
  - Today: holds.
- [ ] **KM11** `00:01:51,050` "If planning every break starts to feel compulsory, that is something to record about the cost."
  - Direction: same-day.
  - Points to: D5 step 3, "Chunking everything is a way of talking"; D5 step 7, "the cost line is the one worth writing carefully."
  - Must stay true: the log has a cost line; the plan-versus-habit line stays.
  - Today: holds.
- [ ] **KM12** `00:01:59,110` "After the short check, the activity starts with that example line."
  - Direction: forward.
  - Points to: D5 step 5 quiz (two questions), then D5 step 6, "Read this line out loud first ... I am going / to the store / to buy some bread."
  - Must stay true: QUIZ directly after the VIDEO; the activity opens with the example line.
  - Today: holds.
- [ ] **KM13** `00:02:03,970` "Then you choose a short paragraph and read it aloud once, on your own."
  - Direction: forward.
  - Points to: D5 step 6, "pick a short paragraph ... and read it out loud once".
  - Must stay true: one paragraph, read once, alone.
  - Today: holds.
- [ ] **KM14** `00:02:09,670` "The trial log records your chosen test, the result, and the cost."
  - Direction: forward.
  - Points to: D5 step 7 log, "Which test you picked, what you expected before you started, whether it passed, what it cost you".
  - Must stay true: a trial log after the activity with test, result and cost.
  - Today: holds.
- [ ] **KM15** `00:02:15,270` "Those details help you decide whether the breaks earned a place in your reading."
  - Direction: forward.
  - Points to: D5 step 7 "Keeping it?"; D8 "Keep what earned a place."
  - Must stay true: the phrase "earned a place" and the keep decision.
  - Today: holds.

**Shared facts and examples (not rows).** Pip's note: "The breaks felt less
effortful, but I lost the meaning."
