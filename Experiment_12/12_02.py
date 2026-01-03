# To implement a Python program that demonstrates various string functions
# using a menu-driven approach.

def string_operations(s):
    while True:
        print("\n------ STRING OPERATIONS MENU ------")
        print("1. Convert to Uppercase")
        print("2. Convert to Lowercase")
        print("3. Capitalize String")
        print("4. Title Case")
        print("5. Find Substring")
        print("6. Replace Substring")
        print("7. Count Character")
        print("8. Check String Type")
        print("9. Split String")
        print("10. Remove Extra Spaces")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            print("Uppercase:", s.upper())

        elif choice == "2":
            print("Lowercase:", s.lower())

        elif choice == "3":
            print("Capitalized:", s.capitalize())

        elif choice == "4":
            print("Title Case:", s.title())

        elif choice == "5":
            sub = input("Enter substring to find: ")
            print("Position:", s.find(sub))

        elif choice == "6":
            old = input("Enter word to replace: ")
            new = input("Enter new word: ")
            print("Updated String:", s.replace(old, new))

        elif choice == "7":
            ch = input("Enter character: ")
            print("Count:", s.count(ch))

        elif choice == "8":
            print("Is Alpha:", s.isalpha())
            print("Is Digit:", s.isdigit())
            print("Is Alphanumeric:", s.isalnum())
            print("Is Lower:", s.islower())
            print("Is Upper:", s.isupper())

        elif choice == "9":
            print("Split String:", s.split())

        elif choice == "10":
            print("Trimmed String:", s.strip())

        elif choice == "11":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


# Main program
string = input("Enter a string: ")
string_operations(string)
