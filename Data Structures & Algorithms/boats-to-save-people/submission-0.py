class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        L, R = 0, len(people)-1

        while L <= R:
            total = people[L] + people[R]
            if total > limit:
                boats += 1
                R -= 1

            else:
                boats += 1
                L += 1
                R -= 1


        return boats

            