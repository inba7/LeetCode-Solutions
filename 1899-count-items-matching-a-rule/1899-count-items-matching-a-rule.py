class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        Count = 0
        if ruleKey == "type":
            ruleKey = 0
        elif ruleKey == "color":
            ruleKey = 1
        elif ruleKey == "name":
            ruleKey = 2
        for item in items:
            if item[ruleKey] == ruleValue:
                Count += 1
        return Count