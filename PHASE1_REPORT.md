# Phase 1 report: content extraction

Sources:
- `CSCS Health, Safety & Environment Test Prepration 2026-2027 COPY.docx`: front matter, Diagnostic Quick Test, 10 chapters and Practice Tests 1–7.
- `Practice-Test-Questions.pdf`: Practice Tests 8–20.

Nothing has been invented, reworded or "corrected". Every value below comes from the manuscript.

## Counts

| Item | Instruction expects | Extracted | File |
|---|---|---|---|
| Practice test questions | 1,000 (20 × 50) | 1,000 | `data/questions_all.json` |
| Diagnostic Quick Test | 15 | 15, each with a "Chapter to revise" tag | `data/questions_all.json` (ids `diag-q1`…) |
| Image questions | 5 per test | 100 in tests + 4 in diagnostic | `images/questions/` |
| Subchapters | 50 | 50 | `data/subchapters.json` |
| Exam Alerts | 50 | 50 | `data/subchapters.json` |
| Common Mistakes | 50 | 50 | `data/subchapters.json` |
| Memory Aids | 50 | 50 | `data/subchapters.json` |
| Quick Checks (with answer) | 36 | 36 | `data/subchapters.json` |
| "How this gets tested" | 50 | 50 | `data/subchapters.json` |
| Chapter Check-Ups | 10 × ~7 | 10 × 7 = 70 (20 multiple choice, 20 fill-in-the-gap, 20 open-ended, 10 true/false) | `data/chapter_checkups.json` |
| Table 6.1 (sign categories) | 5 rows | 5 rows | `data/table_6_1.json` |
| Front matter sections | 8 named | All present (plus "What's Actually Tested" and "Ready to Begin") | `data/front_matter.json` |

Every question record holds: id, book reference ("Test 12, Q31"), stem, four options, the correct letter **taken from the printed answer key**, explanation, one "why it fails" line per wrong option, the COMMON MISTAKE line, and the image path for image questions.

Correct-answer letters across the 1,015 questions: A 256, B 250, C 255, D 254. No option uses position-dependent wording ("all of the above", "both A and B").

## Problems found in the manuscript

These need the owner's decision. None has been fixed by guessing.

1. **No chapter tags on the 1,000 practice questions.** Only the 15 diagnostic questions carry "CHAPTER TO REVISE". The instruction needs a chapter on every question: for the chapter totals in 6.1, the per-50 exam mix, readiness, and "Chapter to revise" on the review screen.
   - Tests 1–7 appear to be ordered in chapter blocks that match the per-test mix (Q1–5 Ch1, Q6–9 Ch2 … Q47–50 Ch10). A few spot checks fit, but this is an inference, not a printed tag.
   - Tests 8–20 are mixed in order, so no position rule applies.
   - **Needed:** the chapter tag for each question from the author's source data. Otherwise the owner must approve a chapter list that Claude drafts by matching each question to its subchapter.
2. **No Diagnostic score-band page.** Section 6.3 asks for "the same score bands as the book", but neither file contains a score-band page. **Needed:** the score bands, or approval to show the raw score with the chapters to revise and no bands.
3. **Test 14, Q13 has only three options (A–C) in the PDF.** The answer key has a "D:" reason, so option D was lost from the question page. It is excluded until the owner supplies option D.
4. **Test 2, Q50 and Test 7, Q50 have no COMMON MISTAKE line** in the answer key. Each will only be used if the line is supplied, or the owner accepts it without one.
5. **Test 1, Q32 has no question number in the manuscript.** The line starts ". A scaffold was inspected…". It is unambiguous, so it was kept as Q32 and is logged here so the book can be fixed.
6. **Three question images are over 250 KB** (the largest is 412 KB). They will be recompressed in the build. All 104 images are 16:9.

## Smaller notes for the owner

- "How to Use This Guide" describes the Chapter Check-Ups as "multiple choice, fill-in-the-gap, and short open questions", but each check-up also contains a true/false item.
- The front matter states 45 minutes, 50 questions and a 90% pass mark (45 of 50). As section 15 requires, these still need confirming against current CITB information before launch.
- The front matter says the guide includes "drag-and-drop style questions" among the 1,000. No drag-and-drop item was found in the 20 tests; all 1,000 are four-option multiple choice.

## Not checked yet (later phases)

- Viewing every image against its question and explanation (section 7.2). This is part of the Phase 2 selection.
- Acronyms and key numbers for the reference pages (Phase 6).

## Still needed from the owner

1. A decision on the chapter tags (problem 1). This blocks Phase 2.
2. The Diagnostic score bands (problem 2).
3. Option D for Test 14, Q13, and the two missing COMMON MISTAKE lines (optional).
4. The five login background images (section 5).
5. The hosting domain (can come last).
