# Linear Search using Static Data

def linear_search(arr, key):
 for i in range(len(arr)):
  if arr[i] == key:
   return i
 return -1

# Static array
arr = [10, 25, 30, 45, 60, 75]
key = 45

print("Array:", arr)
print("Element to search:", key)

result = linear_search(arr, key)

if result != -1:
  print("Element found at position:", result + 1)
else:
 print("Element not found")
