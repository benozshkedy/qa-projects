# Test Case: Prevent Adding Duplicate Course (Negative)

**Test Case ID:** LMS-1.1.2.2-N  
**Module:** Course Management  
**Type:** Negative  
**Priority:** Medium  
**Test Level:** System Testing  
**Tool Used:** TestRail  

---

## Objective

Verify that the system prevents adding a course
when duplicate data (Code + Department) already exists.

---

## Preconditions

1. Admin user credentials are available.
2. An existing course record is stored in the database.
3. The existing course details (Code + Department) are known.

---

## Test Steps

1. Log in as Admin.
2. Navigate to the "Table Management" screen.
3. Open the "Course Management" tab.
4. Click the "Add" button.
5. Enter duplicate values:
   - Existing Course Code
   - Existing Department
6. Click the "Submit" / "Execute" button.
7. Confirm the displayed error message (if prompted).
8. Return to the courses list.

---

## Expected Result

- The system blocks the operation.
- An appropriate validation error message is displayed.
  (e.g., "Duplicate course values are not allowed.")
- The system remains on the Course Management screen.
- The duplicate course is NOT added to:
  - The database
  - The courses list

---

## Validation Focus

- Duplicate validation logic
- Database integrity
- Error handling
- UI feedback accuracy

---

## Business Rule Verified

The combination of Course Code + Department must be unique.
Duplicate entries are not permitted.