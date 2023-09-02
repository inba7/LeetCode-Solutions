class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
class Solution(object):
    def minExtraChar(self, s, dictionary):
        trie = self.buildTrie(dictionary)
        words = set(dictionary)
        dp = [0] * (len(s) + 1)
        for start in range(len(s) - 1, -1, -1):
            dp[start] = 1 + dp[start+1]
            current = trie
            for end in range(start, len(s)):
                if s[end] not in current.children:
                    break
                current = current.children[s[end]]
                if current.is_word:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]
    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.is_word = True
        return root