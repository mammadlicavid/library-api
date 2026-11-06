
# Library API Refactoring Report

## 1. Design Problems Identified

### Problem 1: Low Cohesion

In the original `app.py`, almost everything was written in one file. It handled database operations, API requests, validation, notifications, and library rules. This is a cohesion problem because these tasks have different purposes. It makes the code harder to understand and change because modifying one part might affect another.

### Problem 2: Shared Global Variable

The original code used a global variable called `CURRENT_MEMBER`, which could be accessed by different functions. This is called common coupling. It can cause problems because changing the variable in one function might affect another function unexpectedly. It also makes finding errors more difficult.

### Problem 3: Repeated Database Connections

In the original `app.py`, many functions opened their own SQLite database connections. This is an example of external coupling because different parts of the code directly depended on the database. If we wanted to change how the database works, we would have to update many functions instead of just one.

### Problem 4: Validation Function

The original code had a function called `check(value, kind)`, which performed different checks depending on the `kind` argument. This is called control coupling. It makes the code harder to maintain because adding a new type of validation means changing the same function, which could affect existing checks.

### Problem 5: Notification Function

The original code also used a function called `notify(kind, ...)` to handle different notifications. This is another example of control coupling because the function's behavior depends on the `kind` argument. If we wanted to add a new notification or change an existing one, we would need to modify this shared function, which could introduce errors.

## 2. Before and After Measurements

The goal of the refactoring was to make the code easier to understand and change without affecting how the API works.

| Measurement | Before | After |
|---|---|---|
| Tests passing | 53/53 | 53/53 |
| Lines in the largest file | 555 | 520 |
| Number of application Python files | 1 | 4 |
| Places where the fine rate appears | 7 | 1 |
| Route handlers containing SQL | 16 | 12 |
| Can fine calculations be tested without HTTP or a database? | No | Yes |
| Places edited for the instructor's change request | N/A | Not assigned yet |

After refactoring, the application was divided into four files: `app.py`, `database.py`, `book_repository.py`, and `fines.py`. The database connections were centralized, book-related SQL was moved into a separate repository, and the fine calculation was placed in its own module.

The largest file became smaller, and all 53 tests continued to pass. This shows that the code was improved without changing the API's expected behavior.

## 3. Reflection Questions

### Question 1: Which module is the most cohesive? Describe its one job in a sentence.

I think `fines.py` is the most cohesive module because it has one clear responsibility, which is calculating fines for overdue books. It does not need to handle database connections or API requests, so its code is simple and easy to understand.

### Question 2: Which dependency did you remove, and what can now change independently because of that?

I removed the direct dependency between the book API routes and the SQLite database queries. Before refactoring, the routes contained SQL statements. Now, the book queries are handled by `book_repository.py`. This means I can change how book data is accessed without changing the book routes, as long as the repository functions continue to return the same results.

### Question 3: What coupling remains, and why did you accept it?

Some coupling still exists because `app.py` handles API requests, validation, notifications, and some database operations. I accepted this because the goal was to improve the code step by step rather than rewrite the entire application. I focused on separating the database connections, book operations, and fine calculations while keeping all 53 tests passing.
