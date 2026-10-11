# What the app actually does

Program text makes promises about the product: the interviewer waits, the app
reminds you, your answer comes back later. Each promise must be true of the
code today. The Interview Ready review (October 2026) found the same class of
fault again and again: a sentence that described how we wanted the app to
behave, not how it behaves.

Before a sentence says what the app, a call or an AI character will do, find
the code that does it. The table below is a starting point, checked on
2026-10-11. Code changes, so confirm the file before you rely on a row. If a
row is wrong, fix this file in the same change.

Paths are relative to sw-be-2 unless they start with `app/`, which means
sw-fe-m-2.

## Calls

| Behaviour | What is true | Where |
|---|---|---|
| Silence during a block | After about 1 second of silence the turn ends and the AI replies. A short pause is treated as "maybe unfinished", so the AI replies briefly and invites the person to go on. It does not talk over a word, but it does not stay silent for long either. | `src/services/stt.deepgram.service.ts` (endpointing 800 ms, utterance end 1000 ms), `src/index.ts` (`utterance_end` note to the AI) |
| A long silence | With the call screen open, the AI checks in kindly after 30 seconds and pauses the call after 60 seconds. | `src/config/PhoneCallConfig.ts` (`IDLE_*_PRESENT_MS`) |
| "Take your time" button | When it is on, silence never ends the turn. The person taps "I'm done" to hand back. The button is an icon with no label, and no program text mentions it. | `app/components/CallingWidget.tsx` |
| An interruption | The AI can only speak in a pause after a sentence. It cannot cut in while the person is talking. Someone who never pauses may not get the interruption a day promises. | Same as above |
| Panel calls | Day 13 of Interview Ready is two people, Ananya and Rohit, each with their own voice. Code decides who speaks next, one at a time. | `src/seed/exposure/interviewReady.ts` (`PANEL_DATA`) |
| Headphones | Every AI call needs headphones. Without them the call does not start. | `app/util/functions/headset.ts` |
| Cost | A call costs one call credit. A program's own call never runs as the free weekly call. | `src/services/practiceActivity.service.ts` (`startActivity`) |

So: write "they wait and do not talk over you", never "completely, silently,
for as long as it takes". Write "the silence, left for you to fill", never
"left sitting there until you fill it".

## Program steps

| Behaviour | What is true | Where |
|---|---|---|
| Stamina | A program step costs no stamina. The same activity opened from Explore does. | `practiceActivity.service.ts` (`startActivity`, `packId` check) |
| The day's own words | `instructionsOverride`, `encouragementOverride`, `completionPromptOverride` and `completionPlaceholderOverride` show on the day card and on the step screen after Start. The library row is copied, never edited. | `pack.service.ts` (`applyDrillCopyOverrides`), `practiceActivity.service.ts` (`applyProgramDayCopy`) |
| Reframe in a program | Shows only the day's own thought series. The shuffle button moves between that series' thoughts. The series switcher is hidden. The day's `completionPromptOverride` shows above the writing box and the placeholder inside it. | `app/screens/.../CognitivePractice/Reframe/index.tsx` |
| Finish screens | In a program the finish screen has one way out: Done, back to the day. No Explore More, share, reminder, avatar studio, "try something easier" or Settings link. | `DonePractice`, `MirrorWork/SummaryScreen.tsx`, `RealLifeChallenge`, `HardModeToggle` |
| The goals list | Required in every program that has a goal harness. A day does not open until the list exists. | `src/seed/pack/goalHarness.ts`, `app/screens/Programs/GoalsAsk` |
| Recall questions | One question is drawn from the pool. A `when` map on the QUIZ block can pick the question that matches an earlier form answer. | `ModuleContentBlock.ts` (`QuizBlockContent.when`), `pack.service.ts` |

## What the person sees again later (readback)

Only these places show a person their own earlier words. Promise readback
nowhere else.

- Keepsake forms, and the last-day `WEEK_REVIEW` block.
- The GOALS block, and the "ON YOUR LIST" card on the Home screen.
- A FORM with `recallFrom`, which shows earlier answers above its fields.
- The saved Reframe reply, shown on the finished step as "When you think" and
  "Your reply". It is always shown with the thought it answers.

A skipped step is recorded as a choice. The day stays open and can be done
later, but nothing reminds the person about a skipped step. Write "you can
come back to it at any time", never "the app will ask again".

Reminders about the list are on the Home screen only. After 14 days without
progress the Home card asks about it again. There is no push notification for
the list (`homePriorityCard.service.ts`, `GOAL_WAITING_DAYS`). Write "We
remind you about them on your Home screen", never "the app keeps asking".

## Words filled in for each person

| Token | Where it can go | Filled with | Empty fallback |
|---|---|---|---|
| `{{namedGoals}}` | TEXT `markdown` | The person's list, in rank order, joined ("a, b and c") | `noGoalsText` replaces the whole `##` section |
| `{{firstGoal}}` | ACTIVITY `descriptionOverride`, `instructionsOverride`, `encouragementOverride` | The first goal, worded as the list shows it ("Get through the recruiter") | The same field in `noGoals` |
| `{{copyButton}}` | TEXT `markdown`, with `content.copy` | A Copy button for `copy.text` | None needed |

Tests require a fallback for every token in Interview Ready
(`src/tests/namedGoals.test.ts`). Give every new use one, even when the list
is required: the fallback stops a broken page if a read fails.

## How text is drawn

The renderer is `app/components/Pack/SimpleMarkdown.tsx`.

- Headings `#` to `####`, `> ` quotes, bullet and numbered lists, checkboxes,
  bold, italic and links. No tables, images, code blocks or nested lists.
- A blank line ends a list item. Only an indented line after the blank line
  continues the item. Until 2026-10-11 any paragraph after a list joined its
  last item (36 places in 8 programs), so check old screenshots with care.
- A `###` or `####` heading takes its own spacing. A blank line next to it
  adds nothing.
