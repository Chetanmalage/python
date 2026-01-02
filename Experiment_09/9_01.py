# Develop a real-time application using Lists and Tuples to manage product
# information in a shopping system.
# Your program should demonstrate:
#     1. Creation of Lists and Tuples
#     2. Storing multiple records
#     3. Traversing Lists and Tuples
#     4. Searching and deleting records
#     5. Difference between mutable and immutable data structures


# Step 1: Global List (Mutable)
products = []   # List to store product records


# Step 2: Functions

def add_product():
    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Quantity: "))

    # Tuple (Immutable)
    product = (pid, name, price, quantity)
    products.append(product)
    print("Product added successfully.")


def display_products():
    if not products:
        print("No products available.")
        return

    print("\nProduct Inventory:")
    for p in products:   # Traversing List of Tuples
        print("ID:", p[0], "Name:", p[1],
              "Price:", p[2], "Qty:", p[3])


def search_product():
    pid = int(input("Enter Product ID to search: "))
    for p in products:
        if p[0] == pid:
            print("Product Found:", p)
            return
    print("Product not found.")


def delete_product():
    pid = int(input("Enter Product ID to delete: "))
    for p in products:
        if p[0] == pid:
            products.remove(p)   # List is mutable
            print("Product deleted successfully.")
            return
    print("Product not found.")


def tuple_operations():
    if not products:
        print("No products available.")
        return

    sample = products[0]
    print("Sample Product Tuple:", sample)

    print("Index of Price:", sample.index(sample[2]))
    print("Count of Quantity:", sample.count(sample[3]))


# Step 3: Menu-Driven Program

def main():
    while True:
        print("\n---- PRODUCT MENU ----")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Delete Product")
        print("5. Tuple Operations")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            tuple_operations()
        elif choice == "6":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
