# Test Case: Update Book in "Available" Status

**Test Case ID:** LMS-1.1.2.2  
**Module:** Book Management  
**Type:** Functional  
**Priority:** Medium  
**Test Level:** System Testing  
**Tool Used:** TestRail  

---

## Objective

Verify that a book in "Available" status can be updated successfully
without changing its status.

---

## Preconditions

1. User is logged into the system.
2. A book exists in the system with:
   - Valid Book Code
   - Status = "Available"

---

## Test Steps

1. Navigate to the "Update / Cancel Book" screen.
2. Enter an existing Book Code.
3. Verify that the book details are loaded correctly.
4. Confirm that the status displayed is "Available".
5. Select the "Update" option.
6. Modify one or more editable fields (e.g., Book Name, Author, Subject).
7. Click the "Confirm" button.
8. Approve the confirmation message (if prompted).
9. Search for the updated book again.

---

## Expected Result

- The system validates the input successfully.
- A success message is displayed:  
  **"The book was updated successfully."**
- Updated data is saved and displayed correctly.
- The book status remains **"Available"**.
- No unintended status change occurs.

---

## Validation Focus

- Field editability
- Data persistence
- Status integrity
- Confirmation flow

---

## Business Rule Verified

Updating book details must not alter its availability status.