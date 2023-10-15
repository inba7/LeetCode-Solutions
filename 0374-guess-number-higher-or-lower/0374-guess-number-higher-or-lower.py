class Solution(object):
    def guessNumber(self, n):
        Start, End = 1, n
        while Start <= End:
            Mid = Start + (End-Start)//2
            if guess(Mid) == 0:
                return Mid
            elif guess(Mid) == -1:
                End = Mid - 1
            else:
                Start = Mid + 1
        return -1 