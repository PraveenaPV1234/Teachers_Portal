                                Teacher Portal

This is a web-based application built with Python, Django, HTML, Javascript. It allows teachers to log in, manage student records, and perform operations like adding, editing, deleting, and viewing student data.

Core Features (as per requirements)

1.Login Authentication

    Secure login for teachers

    User validation with error handling

2.Teacher Dashboard
    Lists all students with subjects and marks

    Inline edit and delete options for each record

3.Add Student via Modal

    Modal form for adding new student data

    Handles duplicate entries (updates marks if student+subject already exists)

4.Extra Features Implemented

    1.Pagination

        Neatly paginated student listing

        Easy navigation with "Previous" and "Next" buttons

    2.Pass/Fail Badge

        Automatically displays a Pass or Fail tag based on marks

        Visually highlights performance

    3.Grade System with Color Coding

        Grades assigned dynamically:

        A+ for 90+

        A, B, C, D, and F accordingly

        Colored labels make it easy to interpret performance

    4.Alphabetical Sorting by Name

        Students appear in ascending order for faster lookup

Technologies Used

    Backend: Python, Django

    Frontend: HTML, TailwindCSS, Alpine.js

    Database: SQLite (or compatible with Django ORM)

Improvements

    1. Search and Filter

    By student name, subject, or pass/fail status

    2. CSV Export

    Export student data for offline usage

    3. Performance Analytics

    Average, highest, and lowest marks by subject

    4. Profile Photo Support

    Upload student images (optional)

    5. Role-Based Access Control

    Different views for Admins and Teachers

Setup Instructions 

    git clone https://github.com/PraveenaPV1234/Teachers_Portal.git
    cd project-folder
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

