# Localization – Test Cases

**Project:** PlayStation Israel  
**Focus:** Language & Region Validation

---

## TC-49 — All Key Pages Load in Hebrew
**Priority:** Medium  
### Steps
1. Navigate between main pages
### Expected Result
- All content in Hebrew
- No mixed language

---

## TC-50 — Language Switch Works
**Priority:** Medium  
### Steps
1. Switch to English
2. Switch back to Hebrew
### Expected Result
- Language updates correctly
- RTL restored when Hebrew selected

---

## TC-51 — Region Preserved Across Navigation
**Priority:** Medium  
### Steps
1. Navigate via menus and back button
### Expected Result
- il-he remains in URL
- No locale switch