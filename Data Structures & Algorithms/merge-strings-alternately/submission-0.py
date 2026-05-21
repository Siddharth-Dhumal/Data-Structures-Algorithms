class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2

        if not word2:
            return word1

        l, r = 0, 0
        result = ""

        while l < len(word1) and r < len(word2):
            result += word1[l]
            result += word2[r]
            l += 1
            r += 1
        
        if l:
            while l < len(word1):
                result += word1[l]
                l += 1
        
        if r:
            while r < len(word2):
                result += word2[r]
                r += 1
        
        return result