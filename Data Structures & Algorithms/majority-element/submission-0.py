class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for k, v in freq.items():
            length = freq[k]
            if length > len(nums) // 2:
                return k