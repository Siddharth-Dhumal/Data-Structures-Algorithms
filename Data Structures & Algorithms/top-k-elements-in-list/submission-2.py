class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums) + 1)]
        count_map = {}
        result = []

        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        
        for num, count in count_map.items():
            frequency[count].append(num)

        for i in range(len(frequency) - 1, -1, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result