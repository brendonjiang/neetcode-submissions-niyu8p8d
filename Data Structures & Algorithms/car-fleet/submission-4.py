class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        arr = []
        
        for pos, vel in zip(position, speed):
            arr.append((pos, vel))

        arr.sort(reverse=True)
        groups = 0

        for pos, vel in arr:
            time_to_target = float((target - pos)/vel)

            if stack and time_to_target > stack[0]:
                groups += 1

                while stack and time_to_target > stack[0]:
                    stack.pop()

            stack.append(time_to_target)

        if stack:
            groups += 1

        return groups