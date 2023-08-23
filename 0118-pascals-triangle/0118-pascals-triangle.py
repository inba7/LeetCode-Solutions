class Solution(object):
    def generate(self, numRows):
        Res = []
        for num in range(numRows):
            if(num == 0):
                Prev = [1]
                Res.append(Prev)
            else:
                Current, X = [1], 1
                while(X < num):
                    Current.append(Prev[X-1]+Prev[X])
                    X+=1
                Current.append(1)
                Res.append(Current)
                Prev = Current
        return Res