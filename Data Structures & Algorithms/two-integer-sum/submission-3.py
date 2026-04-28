class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index_map:
                return [index_map[difference], i]
            else:
                index_map[nums[i]] = i