from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):  # Start from the second element
        key = nums[i]  # Current element to be inserted
        j = i - 1  # Index of the previous element

        # Move elements of nums[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        
        # Insert the key into its correct position
        nums[j + 1] = key
    
    return nums

# Example usage:
nums = [12, 11, 13, 5, 6]
sorted_nums = insertion_sort(nums)
print("Sorted array:", sorted_nums)