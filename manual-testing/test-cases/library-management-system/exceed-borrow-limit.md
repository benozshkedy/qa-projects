# Test Case: Prevent Borrowing When Borrow Limit Is Exceeded (Negative)

**Test Case ID:** LMS-1.2.4.5  
**Module:** Borrow / Return Management  
**Type:** Negative  
**Priority:** Medium  
**Test Level:** System Testing  
**Tool Used:** TestRail  

---

## Objective

Verify that the system prevents borrowing a new book
when the reader has already exceeded the maximum allowed
number of borrowed books according to the payment agreement.

---

## Preconditions

1. A reader exists in the system.
2. The reader currently has borrowed books.
3. The number of borrowed books exceeds the allowed maximum.
4. A book exists in the system with status = "Available".
5. User has access to the Borrow / Return screen.

---

## Test Steps

1. Navigate to the "Borrow / Return Books" screen.
2. Enter a valid Reader ID.
3. Confirm that the reader's borrowed books are displayed.
4. Enter the Book Code of an available book.
5. Click the "Borrow" button.

---

## Expected Result

- The system blocks the borrow action.
- The book is NOT added to the borrowed books list.
- The total borrowed books counter does NOT change.
- An appropriate validation error message is displayed, for example:
  **"Cannot borrow more books than allowed by the payment agreement."**
- The book status remains "Available".
- No unintended status change occurs.

---

## Validation Focus

- Business rule enforcement (borrow limit)
- UI error handling
- Counter integrity
- Status preservation
- Data consistency

---

## Business Rule Verified

A reader cannot borrow more books than the maximum allowed
by their subscription/payment agreement.