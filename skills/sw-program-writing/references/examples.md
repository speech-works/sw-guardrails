# Examples

## Plain English: before and after, from real Speechworks lessons

Each pair keeps every fact and number. Use these as the standard for tone and
length. Word counts are per sentence.

**1. Dating, Intimacy & Vulnerability, evidence panel claim (INTERPRETATION_BIAS_ABSENT)**

The founder's example ("Across four studies ... tracks fear of negative evaluation or social anxiety") is an older wording. The current source reads:

- Before (16 + 11 words, 3 abstract terms): "Stuttering on its own has not been shown to shift how people read ambiguous social signals. Where a shift shows up, it tracks fear of negative evaluation."
- After (14 / 13 / 15): "A face or a tone of voice can often mean more than one thing. No study has shown that stuttering alone changes how people read these signals. When a change does appear, it goes with how much the person fears being judged."

**2. The Panic Button, day 1, teach (46 words, one sentence)**
- Before: "The goal is narrower: three short steps and a day to run them before, each step tried once during the week and all three run in order on day seven, so the morning of the thing you dread has you following something you have done before."
- After (4 / 14 / 8 / 9 / 13): "The goal is smaller. You build three short steps, and you choose the day you will use them. You try each step once during the week. On day seven, you do all three in order. So on the morning you dread, you follow steps you have done before."

**3. Interview Ready, day 4, teach (45 words, abstract "the when")**
- Before: "If you are saying it, tick what it is for and write the line, and put the when at the front of it, because "in the first minute" and "if it comes up" are different decisions and only you can see which one you made."
- After (11 / 4 / 9 / 13 / 7): "If you plan to say it, tick what it is for. Then write the line. Start the line with when you will say it. Saying it "in the first minute" and saying it "if it comes up" are different decisions. Only you know which one you made."

**4. Understanding Your Voice, day 2, teach (28 words)**
- Before: "Studies of twins put the genetic share of what makes stuttering more or less likely somewhere between four and eight tenths, and the studies do not agree closely."
- After (14 / 9 / 6): "Studies of twins ask how much of the chance of stuttering comes from genes. Their answers range from four tenths to eight tenths. The studies do not agree closely."

**5. The Speech Toolkit, evidence panel claim (POOLED_ADULT_TRIALS_UNRESOLVED, 27 words)**
- Before: "Pooled across the randomised trials of speaking programs for adults who stutter, the combined effect on speech was small and the range around it included no difference."
- After (15 / 9 / 7 / 13): "Researchers combined the results of the randomised trials of speaking programs for adults who stutter. In these trials, chance decided who got the program. The combined effect on speech was small. Its margin of error was wide enough to include no effect at all."

**6. The Hard Conversations, day 1, quiz explanation (37 words, four clauses)**
- Before: "The relief is real and immediate, which is why the delay repeats, and the version of the call you are imagining is never corrected by anything, because nothing about how the call would actually go ever arrives."
- After (9 / 9 / 11 / 8): "The relief is real, and it comes at once. That is why you keep delaying the call. But you never find out how the call would really go. So the call you imagine is never corrected."

**7. The Art of Disclosure, day 6, teach (32 words, four facts in one sentence)**
- Before: "Hebl and Skorinko (2005) had actors in wheelchairs mention their disability at the beginning, the middle or the end of a job interview, or not at all, and 137 people rated them."
- After (15 / 20 / 5): "In a 2005 study, Hebl and Skorinko used actors in wheelchairs in a job interview. Each actor mentioned the disability at the start, in the middle or at the end, or did not mention it. Then 137 people rated them."

**8. Bouncing Back, day 6, teach (41 words)**
- Before: "That is the link between lying awake going over it and the thing you quietly stopped doing, and it is why a week about the hours afterwards is really a week about what you are still willing to do next month."
- After (16 / 11 / 14): "This links two things: lying awake going over it, and the thing you quietly stopped doing. So this week looks at the hours after a hard moment. But it is really about what you are still willing to do next month."

("Going over it" stays, because Bouncing Back uses "the going over" as its own term from day 1. Rule 6 allows that if day 1 explains it once in plain words.)

## Program faults: before and after

These faults were found by the 2026-09-05 content audit
(`docs/programs/CONTENT_AUDIT_2026-09-05.md` in sw-be-2). The "after" lines
show the shape of the fix. They are patterns to copy, not text to paste.

**9. A bridge in that gives away the recall answer**
- Before: a day 2 recap that says yesterday's finding, "the informative line
  moved six ratings and the apologetic line moved one", directly above a
  recall question asking which wording helps.
- After: name the act and what today does with it. "Yesterday you wrote one
  sentence in your own words. Today you find out whether it is a sentence you
  can say."

**10. A log that cannot hold what the day asks for**
- Before: a block titled "What you expected, and what happened" over a form
  with a Calm-to-Panic rating and an urge-to-hide slider. There was no field
  for what was expected or what happened, and "Panic" names the feeling.
- After: `PROGRAM_REP_LOG`. Did you do the step (yes / a smaller version /
  not today), what you expected, what happened with no adjectives, one line
  to keep.

**11. Positioning said again and again**
- Before: "This program never asked you to do anything, and that was
  deliberate rather than a gap in it." Lines like this appeared more than 100
  times across the shelf.
- After: the day 1 shared promises, once. On later days, cut the line and
  keep the teaching.

**12. A heading that implies the rest is dishonest**
- Before: "The honest version".
- After: name what the section is about, for example "What the study
  measured".

**13. A claim one rung above its evidence**
- Before: "Timing has been measured too", resting on an entry rated WEAK.
- After: "One study looked at timing." Then the entry's limit.

**14. An invented figure**
- Before: "Most abandoned calls are abandoned about ninety seconds in." No
  source had this number.
- After: cut it, or find the source and add an evidence entry first.

**15. A drill screen that undoes the day**
- Before: a library row showing "Take 2 slow breaths" and "That drop is the
  clinical effect of disclosure" one screen after a day that taught the
  opposite.
- After: `instructionsOverride` and `completionPromptOverride` on the paid
  day's ACTIVITY block, written to the day, or a private `PROG_DRILL_*` row.

