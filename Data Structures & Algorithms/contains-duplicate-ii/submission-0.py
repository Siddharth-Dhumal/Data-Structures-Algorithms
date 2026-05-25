class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                duplicate.remove(nums[l])
                l += 1
            if nums[r] in duplicate:
                return True
            duplicate.add(nums[r])
        
        return False