class Solution(object):
    def restoreString(self, s, indices):
        if indices == sorted(indices):
            return s
        return ''.join([Val for Key, Val in sorted(zip(indices, s))])