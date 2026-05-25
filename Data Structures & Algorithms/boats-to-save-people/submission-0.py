class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort()
        l, r = 0, len(people) - 1

        while l <= r:
            remaining_limit = limit - people[r]
            r -= 1
            result += 1
            if l <= r and remaining_limit >= people[l]:
                l += 1
        
        return result