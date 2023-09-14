class Solution(object):
    def predictPartyVictory(self, senate):
        senate = list(senate)
        D, R = deque(), deque()
        for i, s in enumerate(senate):
            if s == "R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            rTurn = R.popleft()
            dTurn = D.popleft()
            if dTurn > rTurn:
                R.append(rTurn + len(senate))
            else:
                D.append(dTurn + len(senate))
        return "Radiant" if R else "Dire" 