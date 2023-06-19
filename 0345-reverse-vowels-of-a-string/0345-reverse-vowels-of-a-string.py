class Solution(object):
    def reverseVowels(self, s):
        N = len(s)
        Left, Right = 0, N - 1
        s = list(s)
        Vowels = list("AEIOUaeiou")
        while Left < Right:
            while Left < Right and s[Left] not in Vowels:
                Left += 1
            while Right > Left and s[Right] not in Vowels:
                Right -= 1
            s[Left], s[Right] = s[Right], s[Left]
            Left += 1
            Right -= 1  
        return "".join(s)