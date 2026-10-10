# Test report: CSCS HS&E Digital Companion, version 1.0.0 (10 October 2026)

Every check in section 16 of the brief was run in Chromium with Playwright, on both copies of the app:

- `index.html` with the `images/` folder
- the standalone `dist/CSCS-HSE-Companion.html`

No browser errors appeared in any run. The only exception is the login test, which deliberately blocks every background photo to test the fallback.

## 1. Content checks
| Check | Result |
|---|---|
| Every question has four distinct options and one correct answer | 315 of 315 (300 bank + 15 diagnostic). The build stops on any failure. |
| Every question has a chapter tag and a book reference | yes |
| All 10 chapters represented | yes |
| Chapter totals match section 6.1 | 30 / 24 / 24 / 30 / 24 / 30 / 48 / 30 / 36 / 24 |
| Every image question has an existing image file | 34 of 34. The build fails if any referenced image is missing. |

## 2. Cross-check against the manuscript
- **Questions:** all 315 questions were re-parsed directly from the printed answer keys:
  - DOCX for Tests 1–7 and the diagnostic
  - PDF for Tests 8–20

  For each one, the correct letter, the explanation and the correct option's text were compared with the app. Result: **315 checked, 0 mismatches.** The only differences were PDF page-break markers inside 7 explanations, which are not part of the text.
- **Flashcards:** all 186 match the chapter text word for word.
- **Drag-and-drop exercises (15), key numbers (53), acronyms (23) and exam-day checklist items (14):** each item carries an exact quote from the manuscript, which is kept in the `data/*.json` files. A script confirmed every quote appears in the manuscript.

## 3. Count checks
| Item | Count |
|---|---|
| Question bank | 300 |
| Sets | 6 × 50 |
| Diagnostic | 15 |
| Flashcards: Exam Alerts / Common Mistakes / Memory Aids / Quick Checks | 50 / 50 / 50 / 36 |
| Drag-and-drop exercises | 15 (6 ordering, 9 matching) |
| Spot the Hazard pictures | 30 |

## 4. Logic tests (hand-worked cases)
| Test | Expected | Result |
|---|---|---|
| Score 45/50 in an exam | "At or above the pass mark" | pass |
| Score 44/50 in an exam | "Below the pass mark" | pass |
| Same seed gives same question and option order (400 seeds) | identical | pass |
| Longest run of the correct answer in the same position (400 exams) | 3 or fewer | 2 |
| Correct-position spread (20,000 questions) | even | 4991 / 4995 / 5028 / 4986 |
| Spaced repetition: new card, "Got it" | box 2, due in 2 days | pass |
| Box 1, 2, 3 and 4, then "Got it" | moves up one box, due in 2, 4, 8 and 16 days | pass |
| Box 5, then "Got it" | stays in box 5, due in 16 days | pass |
| "Missed" from box 4, or a new card "Missed" | box 1, due in 1 day | pass |
| Readiness: 10 answers per chapter, all correct | "Ready to try the mock exam" | pass |
| One chapter at 90% (pass mark) | still "Strong" and "Ready" | pass |
| One chapter at 80% | "Nearly there" | pass |
| One chapter at 70% | "More revision needed" | pass |
| One chapter with only 9 answers | chapter not rated; no overall rating | pass |
| Planner: 10 Oct to 20 Oct, every day | 10 study days, 10–19 Oct, every chapter, Chapter 7 twice, last 2 days light review | pass |
| Planner: short runway (4 days) | all 10 chapters combined into 4 days, plus a plain warning | pass |
| Planner: weekdays only | only Mon–Fri dates (12–16 and 19–23 Oct) | pass |
| Planner: 60 days with Chapter 3 weak | Chapter 3 gets more sessions than Chapter 1; 6 mock-exam days; last 2 days light | pass |
| Planner: start date in the past | rebuilds from today | pass |
| Planner: missed days | "You missed 2 planned days. The plan has been rebuilt from today." | pass |
| Planner: test date in the past, or no study days available | plain message, no plan | pass |
| Calendar file (.ics) | one event per day plus test day; CRLF; lines ≤ 75 octets | pass |
| Certificate eligibility | only full 50-question Exam mode at 45 or more; Sets, practice and 44/50 give none | pass |
| Mistake Bank: wrong, right, wrong, right, right | in, in, in, in, out | pass |

## 5. Login tests
| Test | Result |
|---|---|
| Correct password in any letter case with extra spaces | pass |
| Wrong password; empty password; empty name | rejected with a clear message |
| Remember me (new tab stays signed in) | pass |
| Not remembered (new tab shows sign-in) | pass |
| Sign out | pass |
| Password not stored as readable text anywhere in the file | pass (hash only) |

## 6. Interface checks
- **All 26 screens** were opened in five setups:
  - phone 390 px, light mode
  - phone 390 px, dark mode
  - phone, largest text + high contrast + easier-to-read font
  - phone 360 px, dark + high contrast + large text
  - desktop 1280 px, dark mode

  In every setup there was no sideways scrolling, and all buttons were at least 44 px high.
- **Flashcard study, sign trainer and test runner:** also checked in all five setups.
- **Keyboard only:**
  - a full 50-question exam, from sign-in to results
  - a drag-and-drop exercise
  - sign-in
- **Drag and drop:** tap item then space, tap space then item, mouse dragging, and the keyboard all work. Correct and wrong answers are marked with ✓ or ✗ and words, not colour alone.
- **Reduced motion:** the slideshow uses a plain cross-fade, and the card flip and other animations are turned off.
- **Slideshow fallback:** when every photo fails, there are no broken images and the dark gradient shows.
- **Read aloud:**
  - The button only appears where the browser has speech, and it prefers a British English voice.
  - It can be hidden in Display and reading.
  - The test machine has no speakers, so the voice itself was not heard. What was confirmed is that the button appears and starts speech.

## 7. Print checks
Saved as A4 PDFs in print mode and inspected:

| Page | Pages printed | Result |
|---|---|---|
| Certificate | 1 | clean |
| Flashcard sheet (Chapter 7 filter, 20 cards) | 3, in 2 columns (front and back) | clean |
| Key numbers | 5 | clean |
| Acronyms | 2 | clean |
| Exam-day checklist | 2 | clean |
| Study plan | 3 | clean |

Navigation and buttons are hidden in print.

## 8. Offline check
- **Standalone file:** with the network fully blocked it made **0 network requests**. The login photos, sign-in, all question pictures and every screen worked.
- **Hosted copy:** after the first visit, the service worker had cached 41 files. With the network switched off, a reload still showed the sign-in page with its photos, and question pictures loaded.

## Items dropped
**Key numbers:** 5 entries left out.
- 3 were too general to be useful: the five knowledge areas, five sign categories, and the "three/two ways" counts.
- 2 are inconsistent in the book (see the owner note).

**Questions:** see the Phase 2 report.
- Excluded:
  - Test 18 Q47 (wrong image)
  - the 4 questions with generated parts
- Rejected as unclear images: Tests 1 Q41, 10 Q14, 13 Q38 and 16 Q47.

## Not automated
- Real phones and screen readers (VoiceOver and TalkBack) were not used. Phone sizes were emulated in Chromium.
- Safari and Firefox were not tested.
