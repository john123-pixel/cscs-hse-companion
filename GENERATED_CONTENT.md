# Content written by Claude (owner-approved)

The owner authorised Claude to write content the manuscript does not provide, on the condition that it is accurate. Everything below was written by Claude, not taken from the book. Each item is marked in the data (`generated`, `chapter_source`) so it can be reviewed, changed or removed.

## 1. Fixes to individual questions

| Question | What was missing | Text written | Basis |
|---|---|---|---|
| Test 14, Q13 | Option D (missing from the PDF) | Keep the tablets for workers with headaches and carry on checking the box once a year, replacing the eyewash at the next annual check | Written to match the printed key: "D: Medication is not recommended in a kit and yearly checks are too infrequent." |
| Test 7, Q36 | Option C (correct answer). The manuscript repeats Q35's option C here: "Glasses suit the grinder's flying particles, but the acid handler needs sealed goggles, with a face shield over them for large pours" | Provide a covered, lit walkway or protection fan to keep pedestrians safe from falling items and off the road, agreed with the highway authority | Written from the printed explanation for Q36. |
| Test 2, Q50 | COMMON MISTAKE line (missing from the key) | Treating a small amount of asbestos cement as ordinary waste that can go in a general skip or to a household recycling centre. | Written from the printed explanation and why-wrong lines. |
| Test 7, Q50 | COMMON MISTAKE line (missing from the key) | Judging a dumper's load by how full the skip looks instead of by its weight, and relying on the horn instead of a clear view of the route. | Written from the printed explanation and why-wrong lines. |

## 2. Diagnostic score bands

The manuscript has no score-band page. These bands are in `data/diagnostic_score_bands.json`:

| Score (of 15) | Band | Advice shown |
|---|---|---|
| 14–15 | Strong start | You scored at or above 90%, the pass standard the book describes. Move on to the full practice tests and revise any chapter listed below. |
| 10–13 | Good foundation | Revise the chapters listed below before you start the full practice tests. |
| 0–9 | Build your knowledge first | Work through the ten chapters in order, paying extra attention to those listed below, then take the diagnostic again. |

14 of 15 (93%) is the lowest diagnostic score at or above the book's stated 90% pass standard, so the top band starts at 14. The bands make no prediction about the real test.

## 3. Chapter tags for the 1,000 practice questions

The book prints a chapter only for the 15 diagnostic questions.
- **Test 1** is printed in chapter blocks (Q1–5 Ch1, Q6–10 Ch2, Q11–15 Ch3, Q16–20 Ch4, Q21–24 Ch5, Q25–29 Ch6, Q30–37 Ch7, Q38–42 Ch8, Q43–46 Ch9, Q47–50 Ch10), so its tags follow the book's own order.
- **Tests 2–20** were tagged by Claude reading every question against the chapter and subchapter content. Where a question touches two chapters, it was tagged by the main point its correct answer tests (for example, an RPE fit question goes to Chapter 6, but a silica-dust control question goes to Chapter 4).
- **Check:** applying the same judgement to Test 1 agreed with the book's printed order on 47 of 50 questions. The three differences were borderline cases (RIDDOR with the accident book, competence to inspect a scaffold, and noise health surveillance).
- **For review:** `data/chapter_tags_for_review.csv` lists every question with its tag, so the owner can scan and correct any tag.

Totals across the 1,000 questions:

| Chapter | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Questions | 101 | 63 | 93 | 118 | 63 | 88 | 156 | 107 | 132 | 79 |

Every chapter has more questions than the 300-question selection needs (section 6.1).

## 4. Another manuscript error found while tagging

- **Test 7, Q36:** the correct option C repeated the text of Q35's option C, about safety glasses, so the question had no correct answer about the scaffold. Option C has been rewritten from the printed explanation (see table 1). The book itself should be corrected too.
