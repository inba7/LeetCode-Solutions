class Solution(object):
    def uniqueOccurrences(self, arr):
        Set, Count = set(arr), []
        for i in Set:
            Count.append(arr.count(i))
        if sorted(list(set(Count))) == sorted(Count):
            return True
        else:
            return False