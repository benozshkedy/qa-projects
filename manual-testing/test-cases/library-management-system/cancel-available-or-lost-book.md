# Test Case: Cancel Book in "Available" or "Lost" Status

**Test Case ID:** LMS-1.1.2.4  
**Module:** Book Management  
**Type:** Functional  
**Priority:** Medium  
**Test Level:** System Testing  
**Tool Used:** TestRail  

---

## Objective

Verify that a book with status "Available" or "Lost"
can be successfully cancelled (deleted) from the system.

---

## Preconditions

1. User is logged into the system.
2. A book exists with:
   - Valid Book Code
   - Status = "Available" OR "Lost"

---

## Test Steps

1. Navigate to the "Update / Cancel Book" screen.
2. Enter a valid Book Code.
3. Verify that the book details are displayed.
4. Confirm that the status is either:
   - "Available"
   - "Lost"
5. Select the "Delete" (Cancel) option.
6. Click the "Confirm" button.
7. Approve the cancellation confirmation message.
8. Search for the book again using the same Book Code.

---

## Expected Result

- The system displays a confirmation dialog.
- Upon confirmation, the book is removed from the system.
- A success message is displayed:
  **"The book was successfully cancelled."**
- The book can no longer be found in:
  - The database
  - The search results

---

## Validation Focus

- Status-based action permissions
- Deletion confirmation flow
- Data removal integrity
- System feedback accuracy

---

## Business Rule Verified

Books in "Available" or "Lost" status may be cancelled.
Books in other statuses should not be cancelled.