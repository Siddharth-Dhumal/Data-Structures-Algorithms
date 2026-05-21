class Solution:
    def reorganizeString(self, s: str) -> str:
        frequency = Counter(s)
        prev_char = None
        max_heap = [[-freq, char] for char, freq in frequency.items()]
        result = ""

        for char in s:
            if prev_char and not max_heap:
                return ""

            freq, char = heapq.heappop(max_heap)
            result += char
            freq += 1

            if prev_char:
                heapq.heappush(max_heap, prev_char)
                prev_char = None
            
            if freq < 0:
                prev_char = [freq, char]
        
        return result

            