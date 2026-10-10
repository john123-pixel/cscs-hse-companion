# Phase 4 report: exam, practice, sets, diagnostic and review

## Built
- **Mock exam (section 6.3, part 1).**
  - 50 questions drawn at random from the 300-question bank in the book's chapter mix (5/4/4/5/4/5/8/5/6/4), then shuffled.
  - Timed at 45 minutes from `SETTINGS`, with spoken warnings at 10, 5 and 1 minutes and an automatic submit when time runs out.
  - Flag-for-review, an "All questions" navigator grid, and a confirm step before submitting that shows unanswered and flagged counts.
- **Practice (part 2).**
  - Choose chapters (one or more) and the number of questions: 10, 20, 30, 50, a custom number, or All.
  - Order: random or in sequence. Timer on (exam pace) or off.
  - Feedback after each question, or a review at the end.
  - Option to practise only questions previously answered wrongly. The Mistake Bank screen itself comes in Phase 5.
- **Sets 1 to 6 (part 3).** 50 fixed questions each, with a stable question order and answer options reshuffled on every attempt. Timed like the exam.
- **Diagnostic Quick Test (part 4).**
  - Offered first to new readers on the home screen.
  - 15 questions with no time limit, shown with the score band and the "Chapters to revise" list. The bands are the owner-approved generated ones.
- **Results.**
  - Score and percentage. For 50-question exams and sets, at or below the pass mark (45 of 50, from `SETTINGS`).
  - Results by chapter, and confidence analysis: answers marked "Sure" that were wrong, and correct guesses.
  - Timing: time spent, average per question and the slowest questions.
  - Every result shows: "This is a practice result. It cannot predict your result in the real test."
- **Review (section 6.4).** Laid out like the book's Answer Key:
  - your answer, then the correct answer and explanation
  - "Why the other options are wrong" in grey
  - the highlighted COMMON MISTAKE
  - the chapter to revise and the book reference

  Filters: All, Mistakes, Flagged, Sure but wrong. Options are shown in the order the reader saw them.
- **Report this question** on every question and review item. It opens a pre-filled email to the address in `SETTINGS` (section 13).
- **Navigation.** A bottom tab bar on phones (Home, Practise, More) and a side menu on wide screens. Flashcards and Progress tabs are added when those features exist, so no empty screens are shown.
- **More** contains About, Image credits, Updates and corrections, Privacy, Report a problem and Sign out.
- **Resume.** The attempt is saved after every answer, and "Continue where you left off" appears on the home screen.

## Seeded shuffling (section 6.2)
- Every attempt saves its seed. The question order and option order regenerate exactly from that seed.
- **Correct-answer positions** are spread evenly across the four positions and never land in the same position more than three times in a row.
- **No option letters are shown.** Each question shows its book reference instead.

## Images (section 7)
- 34 images are used: the 30 selected image questions plus 4 diagnostic. All 34 were viewed and checked against their questions.
- Converted to 16:9 WebP, the largest 166 KB, named by book reference (`images/q/t12-q31.webp`).
- Lazy-loaded, each with alt text that describes the scene without giving the answer away (`data/image_alt.json`).

## Files
- `index.html`: about 557 KB, with all content embedded.
- `data/app_data.json`: the embedded content.
- `build/build_data.py` and `build/build_app.py`: rebuild the data and re-embed it.

## Tests run (all passed)
| Check | Result |
|---|---|
| Same seed gives same order and options (400 seeds) | yes |
| Longest run of the same correct position (400 exams) | 2 (limit 3) |
| Correct-position spread over 20,000 questions | 4991 / 4995 / 5028 / 4986 |
| Exam chapter mix and no duplicates (400 draws) | exact |
| Set order stable, options reshuffled | yes |
| Exam at 45/50 | "At or above the pass mark" |
| Exam at 44/50 | "Below the pass mark" |
| Review order rebuilt from the saved seed | matches what the reader saw |
| Time runs out | auto-submits, shows "Time ran out" |
| Reload mid-exam | "Continue" restores the question and flags |
| Practice: chapter 7, 10 questions, instant feedback | 10 Ch7 questions; feedback shows and options lock |
| Diagnostic 10/15 | "Good foundation" plus 5 chapters to revise |
| Keyboard-only full exam (Tab, Enter, 1–4, arrows, submit dialog) | completes |
| Phone 390 px light and dark | no sideways scrolling; image 16:9 |
| Browser errors | none |

## For later phases
- **Phase 5:** flashcards, Mistake Bank screen, sign trainer, drag-and-drop and Spot the Hazard.
- **Phase 6:** home dashboard, readiness, planner, certificate, reference pages, read-aloud and text options, high contrast, and export/import of progress.
