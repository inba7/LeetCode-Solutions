class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        Count = 0
        if ruleKey == "type":
            rk = 0
        elif ruleKey == "color":
            rk = 1
        elif ruleKey == "name":
            rk = 2
        for item in items:
            if item[rk] == ruleValue:
                Count += 1
        return Count