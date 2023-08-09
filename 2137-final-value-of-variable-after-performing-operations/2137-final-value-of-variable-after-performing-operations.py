class Solution(object):
    def finalValueAfterOperations(self, operations):
        Count = 0
        for opr in operations:
            if "+" in opr:
                Count += 1
            else:
                Count -= 1
        return Count