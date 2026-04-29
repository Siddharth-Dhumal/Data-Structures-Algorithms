class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency_map = {}

        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)
        
        for num, freq in frequency_map.items():
            if freq > len(nums) // 2:
                return num