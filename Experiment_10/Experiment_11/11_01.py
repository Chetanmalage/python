# Write and implement a Python program using functions to perform real-time
# operations.
# Your program should demonstrate:
#     1. Function definition
#     2. Function calling
#     3. Passing arguments
#     4. Returning values
#     5. Reusability of functions
#     6. Menu-driven execution

# Step 1: Define Functions

# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)

# Function to calculate average
def calculate_average(total, subjects):
    return total / subjects

# Function to determine result
def determine_result(avg):
    if avg >= 50:
        return "Pass"
    else:
        return "Fail"

# Function to display result
def display_result(name, marks):
    total = calculate_total(marks)
    avg = calculate_average(total, len(marks))
    result = determine_result(avg)

    print("\n----- STUDENT RESULT -----")
    print("Name     :", name)
    print("Marks    :", marks)
    print("Total    :", total)
    print("Average  :", avg)
    print("Result   :", result)


# Step 2: Main Program (Function Calling)

def main():
    name = input("Enter student name: ")
    marks = []

    n = int(input("Enter number of subjects: "))
    for i in range(n):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    display_result(name, marks)


# Calling main function
main()