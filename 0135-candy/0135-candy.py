class Solution(object):
    def candy(self, Ratings):
        Up, Down = 1, 0
        Candy, Peak = 1, 0
        
        for i in range(1, len(Ratings)):
            if Ratings[i] > Ratings[i-1]:
                Up += 1
                Down =  0
                Candy += Up
                Peak = Up 
            elif Ratings[i] == Ratings[i-1]:
                Up, Down, Peak = 1, 0, 0
                Candy += 1  
            else:
                Down += 1
                Up = 1
                Candy += Down
                if Peak <= Down:
                    Candy += 1
        return Candy