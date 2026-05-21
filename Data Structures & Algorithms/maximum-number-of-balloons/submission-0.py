class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_frequency = Counter(text)
        balloon_frequency = Counter("balloon")
        result = len(text)

        for char in balloon_frequency:
            result = min(result, text_frequency[char] // balloon_frequency[char])

        return result