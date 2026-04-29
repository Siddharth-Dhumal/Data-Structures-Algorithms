class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        result = len(nums)
        while i < result:
            if nums[i] == val:
                result -= 1
                nums[i] = nums[result]
            else:
                i += 1
        return result