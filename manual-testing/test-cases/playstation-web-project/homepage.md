# Homepage – Test Cases

**Project:** PlayStation Israel (he-il)  
**Module:** Homepage  
**Test Level:** System / UI  
**Locale:** Hebrew (RTL)

---

## TC-38 — Homepage Loads Successfully
**Priority:** Critical  
### Steps
1. Navigate to https://www.playstation.com/he-il/
2. Wait for page load
### Expected Result
- Homepage loads successfully
- No blank screen
- All main components visible
- No 4xx/5xx errors

---

## TC-39 — Refresh Homepage
**Priority:** High  
### Steps
1. Refresh page (F5 / Cmd+R)
### Expected Result
- Page reloads successfully
- No UI break
- Locale remains he-il

---

## TC-40 — Top Navigation Menu Links
**Priority:** High  
### Steps
1. Click each top menu item (Games / PS5 / PS4 / Services / Plus / Store / Support)
2. Navigate back
### Expected Result
- Each item opens correct page
- No 404 or blank pages
- Locale preserved

---

## TC-41 — Main Banner Link
**Priority:** High  
### Steps
1. Click main banner
### Expected Result
- Redirect to relevant page
- No loading error

---

## TC-42 — Hebrew RTL Layout Validation
**Priority:** Medium  
### Steps
1. Inspect text alignment and layout
2. Verify RTL order
### Expected Result
- Proper RTL layout
- No cutoffs or overlaps

---

## TC-43 — Mobile Responsiveness
**Priority:** Medium  
### Steps
1. Open DevTools → Mobile View
2. Check layout
3. Open hamburger menu
### Expected Result
- No horizontal scroll
- Proper mobile layout
- Hamburger menu works