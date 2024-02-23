class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize a pointer i to track the position for placing the next unique element.
        i = 0

        # Iterate through the array starting from the second element,
        # since the first element is always considered unique.
        for j in range(1, len(nums)):
            # If the current element is different from the last unique element found,
            # it is a new unique element.
            if nums[i] != nums[j]:
                # Move the pointer i forward to prepare for the next unique element's placement.
                i += 1
                # Place the new unique element at the i-th position.
                nums[i] = nums[j]

        # Return the length of the array containing only unique elements.
        # The length is i + 1 because i is zero-based index, and we need to count the number of unique elements.
        return i + 1
