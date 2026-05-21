class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = cur_sum = 0
        prefix_map = { 0 : 1 }

        for num in nums:
            cur_sum += num
            difference = cur_sum - k

            result += prefix_map.get(difference, 0)
            prefix_map[cur_sum] = 1 + prefix_map.get(cur_sum, 0)
        
        return result