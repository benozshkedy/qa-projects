# Test Case: Enter Valid ID for Reader with Borrowed Books

**Test Case ID:** LMS-1.2.4.2  
**Module:** Borrow / Return Management  
**Type:** Functional  
**Priority:** Medium  
**Test Level:** System Testing  
**Tool Used:** TestRail  

---

## Objective

Verify that when entering a valid reader ID for a reader
who currently has borrowed books, the system loads the reader's
borrowed books correctly and enables the appropriate actions.

---

## Preconditions

1. A reader exists in the system.
2. The reader currently has one or more books in "Borrowed" status.
3. User has access to the Borrow / Return screen.

---

## Test Steps

1. Navigate to the "Borrow / Return Books" screen.
2. Enter a valid Reader ID.
3. Confirm the input (press Enter or click Confirm).
4. Observe the displayed reader information.
5. Review the list of borrowed books.
6. Check the state of action buttons.

---

## Expected Result

- Reader details are loaded successfully.
- The list of borrowed books is displayed.
- Selection checkboxes for borrowed books are active.
- The "Return" button is enabled.
- The "Borrow" button is disabled.

---

## Validation Focus

- Reader identification logic
- Status-based UI behavior
- Correct button activation rules
- Data display accuracy

---

## Business Rule Verified

When a reader already has borrowed books:
- Return action must be available.
- Borrow action must be restricted until conditions are met.