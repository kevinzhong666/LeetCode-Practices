nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

class Solution(object):
    def merge(self, nums1, m, nums2, n):
      for j in range(n):
          nums1[m+j] = nums2[j]
      nums1.sort()