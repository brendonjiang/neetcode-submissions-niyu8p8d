class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        days = [0]*len(temperatures)

        temp_stack = []

        for index, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][0]:
                days[temp_stack[-1][1]] = index - temp_stack[-1][1]
                temp_stack.pop()
            temp_stack.append((temp, index))

        return days
