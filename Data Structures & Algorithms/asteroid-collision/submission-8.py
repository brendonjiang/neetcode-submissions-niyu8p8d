class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if stack and ((stack[-1] > 0 and ast > 0) or (stack[-1] < 0 and ast < 0)):
                stack.append(ast)
                continue

            while stack and stack[-1] > 0 and ast < 0 and abs(ast) > stack[-1]:
                stack.pop()

            if stack and stack[-1] == abs(ast):
                stack.pop()
                continue

            elif stack and stack[-1] > 0 and ast < 0:
                continue
                
            else:
                stack.append(ast)



        return stack