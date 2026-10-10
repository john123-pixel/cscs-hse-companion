# Phase 3 report: login and slideshow

`index.html` (single file, inline CSS and JavaScript, no external scripts or fonts) with `images/login/` beside it.

## Login (section 4)
- **Fields:** Name and Password. An empty name is refused.
- **Password check:** not case-sensitive. The entry is trimmed and repeated spaces are collapsed before comparing. Only a SHA-256 hash of the normalised password is stored in the code.
- **Controls:** show/hide password toggle, "Remember me on this device" (ticked by default), Enter submits, and Sign out in the menu.
- **Wording:** the error and independence wording from sections 4 and 14 are used word for word.
- **Profiles:** the name is the profile key, compared ignoring case. Two readers with different names keep separate profiles on the same device.
- **Change from the brief:** the login card does **not** show the publisher's name, because that name *is* the password. The certificate (Phase 6) will show it.

## Slideshow (section 5)
- **Images:** 5 photos changing every 18 seconds (`SETTINGS.slideshowSeconds`).
- **Transitions:** five variants used in rotation (cross-fade, slow zoom, sliding parallax, blur-dissolve and a gentle 3D swing), each lasting 2 seconds.
- **Readability:** a dark gradient overlay, with the login card on a solid surface so the text always meets contrast standards.
- **Loading:** the next image is preloaded. If images fail, a plain dark gradient shows and no broken image ever appears.
- **Motion:** with "reduce motion" switched on, or on a low-powered device, only the cross-fade is used. The slideshow pauses when the tab is hidden.

## Settings block (section 15)
`SETTINGS` at the top of the script holds:
- exam minutes 45, questions 50 and pass mark 45, all **unverified**, so please confirm them against current CITB information
- the spaced-repetition intervals
- the readiness minimum (10), the Mistake Bank exit rule (2 in a row) and the slideshow interval (18 seconds)
- the report email and the version

## Tests run (all passed)
| Check | Result |
|---|---|
| Empty name | refused with "Please enter your name." |
| Wrong password | refused with the friendly publisher-name message |
| `  GreyMINSTER    academic   PRESS ` | accepted |
| Remember me on, then a new tab | stays signed in |
| Remember me off, then a new tab | asks to sign in |
| Sign out | returns to the login page and clears "remember me" |
| Keyboard only (type, Tab, type, Enter) | signs in |
| All five transitions in rotation | crossfade, kenburns, parallax, blur, swing |
| Automatic change after 18 s | yes |
| Reduce motion | cross-fade only |
| All images blocked | dark gradient, no broken images |
| Publisher name visible on the login page | no |
| Phone (390, 360 px), tablet (820 px), desktop (1280 px), light and dark | no overlap, no sideways scrolling |

## Still to do in later phases
- The signed-in screen is only a minimal welcome for now. Exams, practice, sets and review come in Phase 4.
- High-contrast, text size and dyslexia-font options come in Phase 6. The colour tokens for high contrast are already in place.
