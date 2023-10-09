class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        Res = []
        
        for s in spells:
            Left, Right = 0, len(potions)-1
            Index = len(potions)
            while Left <= Right:
                Mid = (Left+Right)//2
                if s * potions[Mid] >= success:
                    Right = Mid - 1
                    Index = Mid
                else:
                    Left = Mid + 1
            
            Res.append(len(potions)-Index)
        
        return Res