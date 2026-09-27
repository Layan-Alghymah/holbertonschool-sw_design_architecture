## Introduction to UML Modeling

General Requirements
Environment:

Ubuntu 20.04

Mermaid-compatible renderer

Use Python-style data types (str, bool, etc.)

File names must match exactly

Do not introduce elements not described in the problem

Do not rename classes, attributes, or methods

Diagrams must be syntactically valid

Only include elements that can be justified from the problem statement

The project will be automatically corrected

## Library Loan System

Each Book has:

a title
an author
a state indicating whether it is available or not (true/false)
Each User has:

a name
an email
When a user borrows a book, a Loan is created.

Each Loan contains:

a start_date
an end_date


## System behavior
The Library must be able to:

add_book to its collection
register_user
create_loan when a user borrows a book
When a loan is created:

the selected book must no longer be available
the loan must reference the book and the user involved
A Book must be able to:

mark_as_unavailable
mark_as_available
A Loan must be able to:

close_loan
When a loan is closed:

the associated book becomes available again
