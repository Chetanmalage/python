# Linear Search using Dynamic Data

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Dynamic input
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter element to search: "))
print("Array:", arr)

result = linear_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")