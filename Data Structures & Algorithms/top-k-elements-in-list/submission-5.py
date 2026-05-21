class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        count = [[] for i in range(len(nums) + 1)]
        result = []

        for num, freq in frequency.items():
            count[freq].append(num)
        
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result