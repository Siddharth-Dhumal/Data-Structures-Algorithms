class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num1 = nums.copy()
        ans = []
        for num in nums:
            ans.append(num)
        for num in num1:
            ans.append(num)
        return ans