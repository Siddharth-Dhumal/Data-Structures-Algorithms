class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")

        for s in tokens:
            if s not in operators:
                stack.append(int(s))

            else:
                r = stack.pop()
                l = stack.pop()
                
                if s == "+":
                    stack.append(l + r)

                elif s == "-":
                    stack.append(l - r)

                elif s == "*":
                    stack.append(l * r)

                else:
                    stack.append(int(l / r))
        
        return stack[-1]