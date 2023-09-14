class Solution(object):
    def removeStars(self, s):
        Out = []
        for char in s:
            if char == "*":
                Out.pop()
            else:
                Out.append(char)
        return "".join(Out)