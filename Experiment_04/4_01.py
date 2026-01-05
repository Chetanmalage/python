# Binary Search using Static Data

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
  
# Static sorted array
arr = [5, 12, 18, 25, 36, 48, 59]
key = 25

print("Array:", arr)

print("Element to search:", key)

result = binary_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
 print("Element not found")