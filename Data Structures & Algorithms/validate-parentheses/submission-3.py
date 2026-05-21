class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        strs = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in strs.values():
                stack.append(c)
            elif c in strs:
                if not stack or stack[-1] != strs[c]:
                    return False
                else:
                    stack.pop()
    
        return not stack