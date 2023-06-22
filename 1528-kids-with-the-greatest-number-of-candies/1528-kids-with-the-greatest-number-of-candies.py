class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        most = max(candies)
        result = []
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= most):
                result.append(True)
            else:
                result.append(False)
        return result