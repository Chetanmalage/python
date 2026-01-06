# Explain the concept of Creating and Instantiating Classes in Python with a suitable
# real-world example. Write a complete Python program to demonstrate:
#     1. Creation of a class
#     2. Use of constructor (__init__)
#     3. Instance variables and class variables
#     4. Creating multiple objects (instantiation)
#     5. Accessing class methods using objects
#     6. Displaying object-specific data


class Student:
    # Class variable
    college_name = "VVP Institute of Technology"

    # Constructor
    def __init__(self, name, roll_no, branch, marks):
        self.name = name        # Instance variable
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks

    # Method to calculate grade
    def calculate_grade(self):
        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    # Method to display student details
    def display_details(self):
        print("College Name :", Student.college_name)
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Branch :", self.branch)
        print("Marks :", self.marks)
        print("Grade :", self.calculate_grade())
        print("-" * 40)


# Creating and Instantiating Objects
student1 = Student("Chetan", 101, "AI & DS", 88)
student2 = Student("Shravani", 102, "CSE", 95)
student3 = Student("Aishwarya", 103, "ECE", 92)

# Accessing methods using objects
student1.display_details()
student2.display_details()
student3.display_details()
