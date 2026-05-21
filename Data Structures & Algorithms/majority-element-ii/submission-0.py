class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for k, v in freq.items():
            if v > len(nums) // 3:
                res.append(k)
        
        if res:
            return res
        else:
            return []
