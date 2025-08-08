def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)   # Sort left half
        merge_sort(right)  # Sort right half
        
        # Merge sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]