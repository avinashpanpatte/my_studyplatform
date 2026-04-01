from app import db, Book, app

with app.app_context():
    # Add sample books
    books = [
        Book(title="Data Structure", subject="Computer Science", description="Syllabus/snippets for Pune University: Arrays, Linked List, Stack, Queue, Tree, Graph. Algorithm analysis, Search, Sorting, Recursion. Study resources: GeeksforGeeks DS notes, CLRS (chapters 10-14)", link="/ds"),
        Book(title="Operating System", subject="Computer Science", description="OS concepts for BSc CS Pune University", link="/os"),
        Book(title="Software Engineering", subject="Computer Science", description="SE principles and practices", link="/se"),
        Book(title="Database Management System", subject="Computer Science", description="DBMS syllabus and resources", link="/dbms"),
    ]
    db.session.add_all(books)
    db.session.commit()
    print("Sample books added to database.")