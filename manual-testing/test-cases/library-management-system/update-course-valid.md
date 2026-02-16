# Test Case: Update Course with Valid Non-Duplicate Data (Positive)

**Test Case ID:** LMS-1.1.4.1  
**Module:** Course Management  
**Type:** Functional  
**Priority:** Medium  
**Test Level:** System Testing  
**Tool Used:** TestRail  

---

## Objective

Verify that an admin can update course details successfully
when the updated values are not duplicate and do not overlap
with existing course records (according to system rules).

---

## Preconditions

1. Admin credentials are available.
2. Access to the courses database/list is available.
3. At least one existing course record is available to update.
4. A set of new course values exists that are:
   - Not duplicate
   - Not overlapping (per business rules)

---

## Test Steps

1. Log in as Admin.
2. Navigate to the "Table Management" screen.
3. Open the "Courses" tab.
4. Select an existing course row.
5. Click "Update".
6. Modify the course details using valid non-duplicate / non-overlapping values.
7. Click "Execute" / "Submit".
8. Approve the confirmation message.
9. Verify the updated course record in the courses list.

---

## Expected Result

- A confirmation message is displayed before applying changes.
- After confirmation, the system updates the course successfully.
- The updated course details are displayed correctly in:
  - The "Courses" list (UI)
  - The database (if verified via DB)
- No duplicate or overlap validation errors appear.

---

## Validation Focus

- Update flow correctness (select → update → execute)
- Validation rules (duplicate / overlap prevention)
- Data persistence
- UI reflects latest data

---

## Business Rule Verified

Course updates are allowed only when the resulting values
do not violate uniqueness/overlap constraints.