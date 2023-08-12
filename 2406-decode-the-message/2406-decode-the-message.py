class Solution(object):
    def decodeMessage(self, key, message):
        key = key.replace(" ", "")
        Keys = dict()
        Inc = 97
        for char in key:
            if char not in Keys and Inc < 123:
                Keys[char] = chr(Inc)
                Inc += 1
        Out = ""
        for Char in message:
            if Char != " ":
                Out += Keys[Char]
            else:
                Out += " "
        return Out