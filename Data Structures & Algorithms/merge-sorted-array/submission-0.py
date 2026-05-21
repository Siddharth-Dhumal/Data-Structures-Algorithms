class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0
        while l < len(nums2):
            nums1[-n] = nums2[l]
            n -= 1
            l += 1
        
        nums1.sort()