class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        frequency = {}
        result = []

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        for num, freq in frequency.items():
            count[freq].append(num)
        
        for i in range(len(count) - 1, -1, -1):
            for num in count[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result