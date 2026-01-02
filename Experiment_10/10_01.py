# Design and implement a real-time application using Sets and Dictionaries to
# manage and analyze data.
# Your program should demonstrate:
#     1. Creation of Sets and Dictionaries
#     2. Set operations (union, intersection, difference)
#     3. Dictionary operations (insert, update, delete, search)
#     4. Real-time data handling
#     5. Menu-driven execution

# Step 1: Define Data Structures

# Dictionary to store student details (Roll No : Name)
students = {}

# Set to store unique courses
courses = set()


# Step 2: Define Functions

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    students[roll] = name        # Dictionary insert/update
    courses.add(course)          # Set insert (unique)

    print("Student added successfully.")


def display_students():
    if not students:
        print("No student records available.")
        return

    print("\nStudent Records:")
    for roll, name in students.items():
        print("Roll:", roll, "Name:", name)


def search_student():
    roll = int(input("Enter Roll Number to search: "))
    if roll in students:
        print("Student Found:", students[roll])
    else:
        print("Student not found.")


def delete_student():
    roll = int(input("Enter Roll Number to delete: "))
    if roll in students:
        del students[roll]        # Dictionary delete
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def display_courses():
    print("Registered Courses:", courses)


def set_operations():
    another_set = {"AI", "ML", "DS"}

    print("Union:", courses.union(another_set))
    print("Intersection:", courses.intersection(another_set))
    print("Difference:", courses.difference(another_set))


# Step 3: Menu-Driven Main Program

def main():
    while True:
        print("\n----- MENU -----")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Display Courses")
        print("6. Perform Set Operations")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_courses()
        elif choice == "6":
            set_operations()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


main()
