class Solution:
    def minOperations(self, s: str) -> int:
        changes = 0

        for i in range(len(s)):
            if i % 2:
                changes += 1 if s[i] == "0" else 0
            else:
                changes += 1 if s[i] == "1" else 0
        
        return min(changes, len(s) - changes)