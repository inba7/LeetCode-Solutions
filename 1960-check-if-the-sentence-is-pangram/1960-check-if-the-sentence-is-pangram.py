class Solution(object):
    def checkIfPangram(self, sentence):
        Flag = True
        for x in range(97, 123):
            if chr(x) not in sentence:
                Flag = False
                break
        return Flag