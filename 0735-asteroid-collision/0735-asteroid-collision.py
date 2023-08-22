class Solution(object):
    def asteroidCollision(self, asteroids):
        Stack = []
        for asteroid in asteroids:
            while Stack and asteroid < 0 and Stack[-1] > 0:
                if abs(asteroid) > Stack[-1]:
                    Stack.pop()
                elif abs(asteroid) == Stack[-1]:
                    Stack.pop()
                    break
                else:
                    break
            else:
                Stack.append(asteroid)

        return Stack