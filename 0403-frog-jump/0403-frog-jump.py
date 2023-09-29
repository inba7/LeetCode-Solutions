class Solution(object):
    def recursiveCanCross(self,stone,jump):    
        if jump < 1:
            return False
        if stone == self.finalStone:
            return True
        
        i = self.stones[stone]
        cacheKey = (jump*2000)+i
        if cacheKey in self.cache:
            return False
        
        if stone + jump + 1 in self.stones:
            if self.recursiveCanCross(stone+jump+1,jump+1):
                return True
            
        if stone + jump in self.stones:
            if self.recursiveCanCross(stone+jump,jump):
                return True
            
        if stone + jump - 1 in self.stones:
            if self.recursiveCanCross(stone+jump-1,jump-1):
                return True
        self.cache.add(cacheKey)
        return False
        
    
    def canCross(self, stones):
        if stones[0]+1 != stones[1]:
            return False
        self.stones = {stone:i for i,stone in enumerate(stones)}
        self.finalStone = stones[-1]
        self.cache = set()

        return self.recursiveCanCross(stones[1],1)