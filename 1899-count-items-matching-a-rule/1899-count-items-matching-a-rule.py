class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        tot = 0
        if ruleKey == "type":
            rk = 0
        elif ruleKey == "color":
            rk = 1
        elif ruleKey == "name":
            rk = 2
        types = [item[rk] for item in items]
        for idx, item in enumerate(types):
            if item == ruleValue:
                tot += 1
        return tot