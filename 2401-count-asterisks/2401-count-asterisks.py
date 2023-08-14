class Solution(object):
    def countAsterisks(self, s):
        return sum([Word.count('*') for Word in s.split('|')][0::2])