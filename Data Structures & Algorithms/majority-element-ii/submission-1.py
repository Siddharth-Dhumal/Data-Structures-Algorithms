class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = {}
        result = []

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        for num, freq in frequency.items():
            if freq > len(nums) // 3:
                result.append(num)
        
        return result