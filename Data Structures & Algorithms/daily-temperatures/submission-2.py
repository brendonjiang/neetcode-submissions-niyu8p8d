class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temps = [0 for _ in range(len(temperatures))]
        
        for idx, temp in enumerate(temperatures):
            
            while stack and stack[-1][0] < temp:
                temps[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()

            else:
                stack.append((temp, idx))       

        return temps