class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            key_array = [0] * 26
            for c in s:
                key_array[ord(c) - ord("a")] += 1
            result[tuple(key_array)].append(s)
        return(list(result.values()))
