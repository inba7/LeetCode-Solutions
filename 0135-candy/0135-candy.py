class Solution(object):
    def candy(self, Ratings):
        Kids, Candy = len(Ratings), [1]*len(Ratings)

        for i in range(Kids-1):
            if Ratings[i] < Ratings[i+1]:
                Candy[i+1] = max(1 + Candy[i], Candy[i+1])
                
        for i in range(Kids-2, -1, -1):
            if Ratings[i+1] < Ratings[i]:
                Candy[i] = max(1 + Candy[i+1], Candy[i])
        
        return sum(Candy)