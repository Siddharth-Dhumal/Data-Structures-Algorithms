class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        freqArr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countDict[num] = 1 + countDict.get(num, 0)

        for num, count in countDict.items():
            freqArr[count].append(num)

        result = []

        for i in range(len(freqArr) - 1, 0, -1):
            for num in freqArr[i]:
                result.append(num)

                if len(result) == k:
                    return result