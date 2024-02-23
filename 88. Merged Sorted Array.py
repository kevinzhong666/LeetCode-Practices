class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Iterate through each element in nums2
        for j in range(n):
            # Place each element of nums2 into the correct position in nums1
            # starting from the index m (end of the initial elements of nums1)
            nums1[m+j] = nums2[j]

        # After all elements of nums2 have been placed into nums1,
        # sort nums1 to ensure the merged array is in ascending order
        nums1.sort()
