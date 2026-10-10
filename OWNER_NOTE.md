# Owner note: CSCS HS&E Digital Companion 1.0.0

## What you have
| File | What it is |
|---|---|
| `dist/CSCS-HSE-Companion.html` | **The whole app in one file** (about 5 MB), with every image built in. Open it in any browser, email it, or upload it on its own. It works with no internet. |
| `index.html` + `images/` + `sw.js` | The same app split into a page, an images folder and an offline helper. This is best for a website, because the first visit loads faster. |
| `data/` | The extracted content for your records: questions, flashcards, drag-and-drop facts, key numbers, acronyms and checklist. Each item quotes the page text it came from. |
| `TEST_REPORT.md` | Results of every check in section 16. |

## Uploading to your domain
**Simplest option:** upload `dist/CSCS-HSE-Companion.html` and rename it `index.html`. Readers then go to your domain and sign in.

**Faster on phones:**
1. Upload `index.html`, `sw.js` and the whole `images` folder to the same folder on your site. Keep the folder names exactly as they are.
2. The site must use **https** for offline use to work. Most hosts, including GitHub Pages, Netlify and Cloudflare Pages, do this for free.

## Changing the pass mark, exam length or question count
1. Open `index.html` (or the standalone file) in a text editor.
2. Search for `const SETTINGS`.
3. Change `examMinutes`, `examQuestions` or `passMark`, then save.

Everything that uses these figures updates by itself: the timer, the pass/fail line, readiness and certificate eligibility.

If you edit `index.html`, rebuild the standalone file with `python3 build/build_app.py`.

## Adding an entry to "Updates and corrections"
1. Search for `function renderUpdates`.
2. Copy the `<h3>…</h3><p>…</p>` pair, put the copy above the existing one, and change the date and text.
3. Change `appVersion` and `buildDate` in `SETTINGS`.
4. Run `python3 build/build_app.py`. Changing the version also makes hosted copies fetch the new version.

## Still to do (only you can do these)
1. **Confirm 45 minutes, 50 questions and pass mark 45 against current CITB information.** These come from the book and have not been independently checked. If CITB differs, correct both the book and `SETTINGS`.
2. **Fix in the book:**
   - Test 1 Q32 is missing a number.
   - Test 7 Q36 option C is copied from Q35.
   - Test 14 Q13 is missing option D.
   - Test 18 Q47 reuses Q8's image.

   None of these questions are used in the app.
3. **Book inconsistencies found while extracting the reference pages:**
   - **Whole-body vibration (4.4):** the text gives 0.5 and 1.15 m/s² A(8), but the 4.4 Memory Aid says the whole-body values are "half" the hand-arm ones (2.5 and 5.0), which would give 1.25 and 2.5. The app uses the main text and leaves the memory aid unchanged, because flashcards quote the book exactly. Please correct the Memory Aid in the book.
   - **Excavations:** the Chapter 8 Learning Objectives say there are "three main ways" to prevent excavation collapse, but 8.1 says "two main approaches".
   - **Ladder 1 m above the landing:** this appears only in the Diagnostic answer key, not in Chapter 7.
4. **Photo credits:** the photographer names for login photos 1, 2 and 4 (Pexels 8961259, 5505125 and 9389356) could not be read from Pexels. They show as "Pexels contributor".
5. **Login photo 3** shows a visible "FIRM GRIP" brand name. Swap it if you prefer no brand.
6. **Domain:** not yet supplied.

## Why the publisher name is encoded in the file
The certificate must show the publisher name, and that name is also the sign-in password. To stop it being found by searching the page source, it is stored encoded rather than as readable text. This is still only a soft gate: anyone determined can get in. That matches the brief.
