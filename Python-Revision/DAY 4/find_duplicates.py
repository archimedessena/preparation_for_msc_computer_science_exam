
import quick_sort
def find_duplicates(nums):
    nums = quick_sort(nums[:])  # Copy and sort
    duplicates = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            duplicates.append(nums[i])
    return duplicates