class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for bracket in s:
            if not stack and bracket in close_to_open:
                return False
            if stack and bracket in close_to_open:
                if close_to_open[bracket] != stack[-1]:
                    return False
                else:
                    stack.pop()
            if bracket in close_to_open.values():
                stack.append(bracket)
        
        return True if not stack else False
        
