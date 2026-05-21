class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in numsSet:
                streak = 1
                while num + streak in numsSet:
                    streak += 1
                result = max(streak, result)

        return result
            