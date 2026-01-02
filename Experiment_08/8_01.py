# Quick Sort using Static Data

def partition(arr, low, high):
    pivot = arr[high] # Pivot element
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

# Static array
arr = [25, 11, 64, 22, 15, 9]
print("Before Sorting:", arr)

quick_sort(arr, 0, len(arr) - 1)
print("After Sorting :", arr)
