# Binary Search using Dynamic Data

def binary_search(arr, key):
 low = 0
 high = len(arr) - 1
 while low <= high:
  mid = (low + high) // 2
  if arr[mid] == key:
   return mid
  elif key < arr[mid]:
   high = mid - 1 
  else:
   low = mid + 1
 return -1

# Dynamic input
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
 arr.append(int(input(f"Enter element {i+1}: ")))

# Sorting is mandatory
arr.sort()

key = int(input("Enter element to search: "))

print("Sorted Array:", arr)

result = binary_search(arr, key)

if result != -1:
 print("Element found at position:", result + 1)
else:
 print("Element not found")