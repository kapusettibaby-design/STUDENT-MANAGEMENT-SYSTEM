students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        print("Student List:")
        for student in students:
            print(student)

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in students:
            print("Student found!")
        else:
            print("Student not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in students:
            students.remove(name)
            print("Student deleted!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
