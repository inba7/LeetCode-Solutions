class SmallestInfiniteSet(object):

    def __init__(self):
        self.seen= [False] * 1005

    def popSmallest(self):
        for i in range(1, 1005):
            if not self.seen[i]:
                self.seen[i] = True
                return i

    def addBack(self, num):
        if num<len(self.seen):
            self.seen[num] = False