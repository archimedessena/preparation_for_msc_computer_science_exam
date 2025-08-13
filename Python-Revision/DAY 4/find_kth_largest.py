def find_kth_largest(nums, k):
    def quick_select(low, high, target):
        if low == high:
            return nums[low]
        pi = partition(nums, low, high)
        if pi == target:
            return nums[pi]
        elif pi < target:
            return quick_select(pi + 1, high, target)
        else:
            return quick_select(low, pi - 1, target)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] >= pivot:  # >= for largest
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    return quick_select(0, len(nums) - 1, k - 1)