class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0 ,len(people) - 1
        boat = 0
        people = sorted(people)
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boat += 1
        return boat        
