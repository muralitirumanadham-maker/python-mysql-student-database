import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="murali@1730",
    database="student_db"
)

cursor = conn.cursor()

print("Connected Successfully")

def add_student():
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    course = input("Course: ")
    marks = int(input("Marks: "))

    query = """
    INSERT INTO students
    (name,age,gender,course,marks)
    VALUES(%s,%s,%s,%s,%s)
    """

    values = (name, age, gender, course, marks)

    cursor.execute(query, values)
    conn.commit()

    print("Student Added")

def view_students():
    cursor.execute("SELECT * FROM students")

    for row in cursor.fetchall():
        print(row)

def search_student():
    sid = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE student_id=%s",
        (sid,)
    )

    result = cursor.fetchone()

    if result:
        print(result)
    else:
        print("Student Not Found")

def update_marks():
    sid = int(input("Student ID: "))
    marks = int(input("New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=%s WHERE student_id=%s",
        (marks, sid)
    )

    conn.commit()

    print("Updated Successfully")

def delete_student():
    sid = int(input("Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE student_id=%s",
        (sid,)
    )

    conn.commit()

    print("Deleted Successfully")

while True:

    print("\n===== STUDENT DATABASE =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        break

    else:
        print("Invalid Choice")
