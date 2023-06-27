class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res