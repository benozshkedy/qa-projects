# PlayStation Web Project – Test Cases Summary

## Overview

This document summarizes the manual test coverage
performed on the PlayStation Israel website (he-il).

Testing focused on functional validation, UI behavior,
localization integrity, and link reliability.

---

## Test Objectives

- Validate correct page loading and rendering
- Ensure navigation flows function properly
- Verify Hebrew RTL layout behavior
- Confirm region (il-he) consistency
- Detect broken or misconfigured links
- Validate mobile responsiveness

---

## Test Coverage Areas

### 1. Homepage

Scope:
- Initial page load validation
- Refresh stability
- Top navigation menu behavior
- Banner redirection validation
- RTL layout inspection
- Mobile responsiveness (DevTools simulation)

Validation Focus:
- No blank screen
- No console errors
- Proper alignment for RTL content
- No unexpected locale switch

---

### 2. Products – PS5 Section

Scope:
- Console information display
- Subpage navigation (Games / Accessories / Controllers / VR2)
- CTA / Purchase button behavior
- Region consistency for Israeli market

Validation Focus:
- Accurate content rendering
- Hebrew language display
- Correct redirection to purchase pages
- No region mismatch

---

### 3. Localization & Language

Scope:
- Hebrew language consistency across pages
- Language switching functionality
- Locale persistence across navigation
- URL validation (il-he)

Validation Focus:
- No mixed-language UI
- Proper RTL restoration after language switch
- No redirect to unintended region (e.g., us-en)

---

### 4. Links Validation

Scope:
- Internal navigation links
- External links behavior
- Broken link detection (404 / 4xx / 5xx)
- New tab behavior validation

Validation Focus:
- All internal links load correct pages
- External links open expected destinations
- No dead links
- Correct tab handling behavior

---

## Test Design Methodology

- Positive testing
- Navigation flow testing
- UI alignment validation
- State validation
- Locale & region validation
- Error detection (HTTP status awareness)

---

## Test Strategy Characteristics

- Manual system-level testing
- Browser-based validation
- Mobile simulation using DevTools
- Hebrew RTL-specific validation focus
- Cross-page navigation stress testing

---

## Tools Used

- Browser DevTools
- TestRail (original documentation)
- VS Code
- Git / GitHub

---

## Conclusion

The executed test cases provided coverage across:

- Functional behavior
- UI stability
- Localization correctness
- Navigation integrity
- Regional compliance

This testing effort demonstrates structured QA thinking,
business rule validation, and attention to UI/UX detail.