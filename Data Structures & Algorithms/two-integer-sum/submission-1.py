class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        imap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in imap:
                return [imap[diff], i]
            else:
                imap[nums[i]] = i