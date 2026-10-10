# Phase 2 report: question selection

The owner needs to approve this list before Phase 3 (login and slideshow) starts.

## Result

- **300 questions** in **six fixed sets of 50**: `data/selection_300.json`, with a readable list in `data/selection_300_for_review.csv`.
- **15 questions from each of the 20 tests.**
- **Chapter totals match section 6.1 exactly:**

| Chapter | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Selected | 30 | 24 | 24 | 30 | 24 | 30 | 48 | 30 | 36 | 24 | 300 |

- **Each set** has the book's per-test mix (Ch1 5, Ch2 4, Ch3 4, Ch4 5, Ch5 4, Ch6 5, Ch7 8, Ch8 5, Ch9 6, Ch10 4) and **5 image questions**.
- **30 image questions** in total: Ch7 11, Ch6 8, Ch9 8, Ch8 2, Ch3 1. The book only has image questions in these five chapters.
- **No two selected questions test the same scenario.** Every pair was compared for wording similarity, and 117 near-duplicate pairs were blocked from appearing together. Examples: two fall-clearance lanyard questions, and two crane radio-signalling questions.
- **Every selected question passed validation:** four distinct options, a correct answer taken from the printed key, a chapter, a book reference, and an existing image file for image questions.
- **Same order every time:** the selection uses fixed random seeds, so it can be reproduced exactly.

## Image check (section 7.2)

46 image questions were viewed against their stem, answer, explanation and wrong-option reasons. 41 passed, and Test 18 Q8 was checked separately and also passed.

**Rejected (not used):**

| Question | Reason |
|---|---|
| Test 18, Q47 | **Manuscript error:** the PDF reuses Test 18 Q8's bricklayer image. The blaster with the air-fed helmet is not shown. A scan of all 104 images found no other duplicate. |
| Test 1, Q41 | The answer depends on "daisy-chained leads", but the image shows only a single lead. |
| Test 16, Q47 | The earbuds the answer depends on are not clearly visible, and the wrong options refer to a mask and glasses that are not in the picture. |
| Test 10, Q14 | Safety glasses "pushed up on his forehead" are not clearly visible. |
| Test 13, Q38 | The explanation says a pedestrian walks "close behind" the forklift, but the image shows the pedestrian in front of it. |

The other 59 image questions were not viewed, so they cannot be selected. They can be checked later if more image questions are wanted.

## Excluded from selection

- **Questions with generated parts:** Test 2 Q50, Test 7 Q36, Test 7 Q50 and Test 14 Q13 are kept in the data but not selected, so every selected question is wholly from the book.
- **Test 18, Q47:** wrong image, see above.

## For the owner

1. Approve the 300, or name any questions to swap. The CSV lists every question by set.
2. **Fix in the book:** Test 18 Q47 needs its own image, of an abrasive blaster in an air-fed helmet with the compressor intake near engine exhaust.
3. **Not done yet (done when the app is built):** the seeded option shuffle and the "no more than three correct answers in the same position in a row" rule are runtime features. They will be built and tested in Phase 4.
