class Solution:
    def reorganizeString(self, s: str) -> str:
        result = ""
        frequency = Counter(s)
        max_heap = [[-freq, char] for char, freq in frequency.items()]
        heapq.heapify(max_heap)
        previous_char = None

        while max_heap or previous_char:
            if previous_char and not max_heap:
                return ""

            freq, char = heapq.heappop(max_heap)
            result += char
            freq += 1

            if previous_char:
                heapq.heappush(max_heap, previous_char)
                previous_char = None

            if freq < 0:
                previous_char = [freq, char]
            
        return result