class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack and stack[-1] > 0:
                    if stack[-1] <= abs(asteroid):
                        while stack and stack[-1]> 0 and stack[-1] <= abs(asteroid):
                            if stack[-1] == abs(asteroid):
                                stack.pop()
                                break
                            stack.pop()
                        else:
                            if not stack or stack[-1] < 0:
                                stack.append(asteroid)

        return stack