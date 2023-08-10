class Solution(object):
    def mostWordsFound(self, sentences):
        Max = 0
        for sentence in sentences:
            sen = sentence.split()
            if len(sen) >= Max:
                Max = len(sen)
        return Max