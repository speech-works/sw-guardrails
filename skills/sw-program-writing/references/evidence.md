# The evidence layer

Every research claim in a program day maps to an entry in
`src/seed/pack/evidence/ProgramEvidence.ts` (sw-be-2). Read that file's header
comment before you add or change an entry. This page is the short version.

## How a day uses an entry

- A TEXT block lists the keys it rests on: `sources: ["DISCLOSURE_OVERALL"]`.
  The database stores only keys, so a citation fix is a deploy.
- **The strength goes in the sentence.** The day says the entry's
  `plainCount` out loud ("Fifteen of eighteen studies found a favourable
  effect"). A count cannot be quietly inflated later the way an adjective can.
- **The source goes at the edge.** The app shows it collapsed, after the
  teaching. Do not write a reference list into the day.
- **The limit comes along.** If the sentence could be read as wider than the
  entry's population or design, the day says the limit, in the words of
  `theLimitInPlainWords`.
- One block never lists the same key twice.

## The fields

| Field | Who reads it | Rule |
|---|---|---|
| `claim` | User | The finding, as narrow as the paper supports |
| `plainCount` | User | The count or size a day says. Plain words, no statistics. Fits in one sentence. |
| `whatItIs` | User | The kind and size of source ("Review of 18 studies"). Describes, never grades. |
| `theLimitInPlainWords` | User | One or two plain sentences. No authors, no p values, no capitals shouting, nothing about our own past mistakes. |
| `source`, `sourceUrl` | User, at the edge | Full citation with a year. PubMed or PMC link preferred. Never one of our own files. |
| `strength` | Tests, console | STRONG, MODERATE, WEAK, CONTESTED or ABSENT |
| `population`, `design` | Reviewer | Who was studied, and how. Say it even when it is inconvenient. |
| `whatItDoesNotShow` | Reviewer only | Mandatory. The limit, every warning and correction. **Never shown to a user.** |
| `sourceRead` | Reviewer | FULL_TEXT or ABSTRACT_ONLY. Abstract only caps the entry at MODERATE. |
| `absenceEvidence` | Reviewer | Needed for any "nobody has measured this" claim |
| `strengthNote` | Reviewer | Why a review or essay is rated above WEAK |
| `lastCheckedAt` | Everyone | The date a person last read the source. Set only by whoever re-read it. |

Every entry also needs a matching entry in `ProgramEvidenceRationale.ts`
(`evidenceSays`, `whyThisWording`, `reviewerFlag`, `priority`). The test
fails without it.

## Rules for writing or editing an entry

- Never widen a claim past its population. Much of the useful anxiety and
  learning research is on students or general clinical samples; say which.
- Published, tested and accepted are three different things. `design` says
  which.
- If the evidence runs both ways, rate it CONTESTED and put both sides in
  `whatItDoesNotShow`. Do not pick the flattering half.
- "Nobody has ever measured this" was written four times and was false all
  four times. Give the source for an absence, or write the narrower true
  sentence ("never tested on people who stutter").
- Every past overstatement was a true finding with its limit dropped. Keep
  the limit.
- Editing an entry means re-reading every day that uses it. Find them with
  `grep -rn KEY src/seed/pack` or the usage list in the review sheet.

## How to read a source from this machine

PubMed pages return a cookie wall to WebFetch and PMC returns a reCAPTCHA. Use
E-utilities from Bash:

```bash
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=ID1,ID2&rettype=abstract&retmode=text"
```

Compare the number, the direction and the population with the entry. An
abstract alone is a MODERATE ceiling. Some PMC full texts load through
WebFetch; Europe PMC's REST `fullTextXML` is another route.

## Words for research copy

- Use the certainty ladder: causes / probably / may / it is unclear whether.
- Use "linked to" or "found with" for a link. Never "causes" or "improves"
  for a finding that only shows a link.
- Never "proven", "breakthrough", "cure", "miracle".
- Report in this order: who was studied, what they did, what they found, the
  limit. One number per sentence.

## Folklore and sources never to use

From PROGRAM_STRATEGY.md Part 11. Never repeat: learning styles, the learning
pyramid, "you forget 80% in 24 hours", the 8-second attention span, "adults
focus for 10 to 15 minutes", Bloom's verb wheels, "under-promise and
over-deliver", "breaking a streak makes people quit", "end on a high and
people forget the middle".

Never cite: the MIDVAS acronym from the 1973 primary text; Sheehan's "five
levels of avoidance"; "60 to 80% relapse" as a measured finding (say
"reported in the literature as"); the self-disclosure conversation study as
Byrd (it is Mancinelli 2019); Yaruss and Quesal (2004) as a *Journal of
Fluency Disorders* paper (it is *J Communication Disorders*). Byrd and
colleagues (2017) had no assertive condition.

## Checks

- `npx jest src/tests/programEvidence.seed.test.ts`: required fields,
  rationale match, banned words, no em dash, `plainCount` length, every key a
  day uses resolves, the plain limit fits on a phone.
- `npm run evidence:review`: regenerates
  `docs/programs/PROGRAM_EVIDENCE_REVIEW.md` from the registry, with per-entry
  usage. Never hand-edit that sheet.
- After a deploy, follow the evidence rollout order in the sw-be-2 docs:
  deploy, then preview, then seed.
