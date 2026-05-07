class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        max_frequency = 0
        l = 0
        frequency = {}

        for r in range(len(s)):
            frequency[s[r]] = 1 + frequency.get(s[r], 0)
            max_frequency = max(max_frequency, frequency.get(s[r]))

            while (r - l + 1) - max_frequency > k:
                frequency[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result