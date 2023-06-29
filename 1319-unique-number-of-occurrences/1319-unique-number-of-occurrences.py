class Solution(object):
    def uniqueOccurrences(self, arr):
        counts=[]
        set_arr=set(arr)
        for x in set_arr:
            if arr.count(x) in counts:
                return False
            else:
                counts.append(arr.count(x))
        return True