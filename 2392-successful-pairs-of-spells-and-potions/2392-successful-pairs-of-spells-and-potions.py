class Solution(object):
    def successfulPairs(self, Spells, Potions, Success):
        Potions.sort()
        Res = []

        M = len(Potions)
        maxPotion = Potions[M-1]

        for Spell in Spells:
            minPotion = (Success+Spell-1) // Spell
            if minPotion > maxPotion:
                Res.append(0)
                continue
            Index = bisect.bisect_left(Potions, minPotion)
            Res.append(M-Index)

        return Res