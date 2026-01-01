# Selection Sort using Dynamic Data

def selection_sort(arr):
 n = len(arr)
 for i in range(n - 1):
  min_index = i
  for j in range(i + 1, n):
   if arr[j] < arr[min_index]:
    min_index = j
  arr[i], arr[min_index] = arr[min_index], arr[i]

# Dynamic input
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
 arr.append(int(input(f"Enter element {i+1}: ")))

print("Before Sorting:", arr)

selection_sort(arr)
print("After Sorting :", arr)