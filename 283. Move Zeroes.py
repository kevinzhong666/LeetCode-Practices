class Solution(object):
    def moveZeroes(self, nums):
        i = 0  # Initialize i for the position of the next non-zero element
        for j in range(len(nums)):  # Iterate through the array with j
            if nums[j] != 0:
                # Move non-zero element to the i-th position
                nums[i] = nums[j]
                if i != j:
                    # Set the original position to zero only if i and j are not the same
                    nums[j] = 0
                i += 1  # Increment i for the next non-zero element's position



