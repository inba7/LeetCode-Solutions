class Solution(object):
    def closeStrings(self, word1, word2):
        set1 = set(word1)
        set2 = set(word2)
        if set1 != set2:
            return False
        list3 = list()
        list4 = list()
        for c in set1:
            list3.append(word1.count(c))
        for c in set2:
            list4.append(word2.count(c))
        return sorted(list3) == sorted(list4)