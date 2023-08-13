class Solution(object):
    def checkIfPangram(self, sentence):
        Sentence = set(sentence)
        return True if len(Sentence) >= 26 else False