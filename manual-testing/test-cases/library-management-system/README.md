# Library Management System – QA Project

This repository contains manual test design and validation
performed on a Library Management System.

The system manages books, courses, and borrowing operations,
with defined business rules controlling status transitions,
uniqueness constraints, and borrowing limits.

---

## System Overview

The system includes the following modules:

- Book Management
- Course Management
- Borrow / Return Management

Testing focused on validating functional flows,
business logic enforcement, and state-based behavior.

---

## Testing Scope

### Book Management
- Update book in "Available" status
- Cancel book in "Available" or "Lost" status
- Status-based action validation

### Course Management
- Update course with valid non-duplicate values
- Prevent adding duplicate courses
- Uniqueness validation (Course Code + Department)

### Borrow / Return Management
- Load reader with borrowed books
- UI state validation (button enable/disable logic)
- Prevent borrowing beyond allowed limit
- Business rule enforcement

---

## Test Design Approach

- Functional testing
- Positive and negative scenarios
- Business rule validation
- State-based testing
- Data integrity verification
- UI behavior validation

---

## Key Business Rules Verified

- Course Code + Department must be unique.
- A reader cannot exceed the maximum allowed borrowed books.
- Books can only be cancelled in specific statuses.
- Status transitions must follow defined system rules.

---

## Repository Structure

library-management-system/
├── test-cases/
├── negative-scenarios/
└── README.md

---

## Tools Used

- TestRail (original test management tool)
- VS Code
- Markdown documentation
- Git / GitHub

---

## Author

Ben Oz Shkedy  
Junior QA Engineer