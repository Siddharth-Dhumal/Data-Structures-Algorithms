class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_chars = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        if not digits:
            return []

        result = [""]
        for digit in digits:
            temp = []
            for s in result:
                for char in num_chars[digit]:
                    temp.append(s + char)
            result = temp
        
        return result