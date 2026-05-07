class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = 0
            if heights[l] <= heights[r]:
                area = heights[l] * (r - l)
                l += 1

            else:
                area = heights[r] * (r - l)
                r -= 1
            
            result = max(result, area)
        
        return result