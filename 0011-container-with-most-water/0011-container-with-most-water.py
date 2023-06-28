class Solution(object):
    def maxArea(self, height):
        l, r  = 0, len(height) - 1
        ans = 0
        h = max(height)
        while l < r:
            x, y = height[l], height[r]
            area = min(x,y) * (r-l)
            ans = max(ans, area)
            if x <= y:
                l += 1
            else:
                r -= 1
            if (r-l)*h < ans:
                break
        return ans
