class Solution(object):
    def reverseWords(self, s):
        words = s.strip().split()
        words.reverse()
        string = str()
        for word in words:
            if string == "":
                string += word
            else:
                string = string + " " + word
        return string