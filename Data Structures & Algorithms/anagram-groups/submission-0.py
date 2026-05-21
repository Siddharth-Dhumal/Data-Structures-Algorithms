class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        resultDict = defaultdict(list)

        for string in strs:

            countArr = [0] * 26

            for character in string:

                countArr[ord(character) - ord("a")] += 1

            resultDict[tuple(countArr)].append(string)

        return list(resultDict.values())