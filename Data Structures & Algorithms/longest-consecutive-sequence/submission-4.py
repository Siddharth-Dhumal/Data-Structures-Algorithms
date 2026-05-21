class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        sequence_set = set(nums)

        for num in nums:
            length = 1
            while (num + length) in sequence_set:
                length += 1
            result = max(result, length)
        
        return result