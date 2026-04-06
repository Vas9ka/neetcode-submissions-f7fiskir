class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)
        i = 0
        j = len(sorted_people) - 1
        ans = 0
        while i <= j:
            capacity = limit - sorted_people[j]
            j -= 1
            ans += 1
            if i <= j and capacity >= sorted_people[i]:
                i += 1
            
        return ans