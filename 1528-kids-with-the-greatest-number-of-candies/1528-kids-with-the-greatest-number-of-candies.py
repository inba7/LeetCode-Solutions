class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        out=[]
        extra_list = [x+extraCandies for x in candies]
        for i in range(0,len(candies)):
            curr_elm=extra_list[i]
            curr_max=max(candies)
            if curr_elm>=curr_max:
                out.append(True)
            else:
                out.append(False)
        return(out)