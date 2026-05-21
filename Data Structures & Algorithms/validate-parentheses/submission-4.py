class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = { ")" : "(", "]" : "[", "}" : "{" }

        for b in s:
            if b in b_map:
                if stack and stack[-1] == b_map[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return True if not stack else False