import bisect
class MyCalendarThree:

    def __init__(self):
        self.kBook = []

    def book(self, Start, End):
        bisect.insort(self.kBook, [Start, 1])
        bisect.insort(self.kBook, [End, 0])
        Result, Curr = 0 , 0
        for X, Y in self.kBook:
            if(Y == 1):
                Curr += 1
                Result = max(Result, Curr)
            else:
                Curr -= 1
        return Result