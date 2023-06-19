class Solution(object):
    def reverseVowels(self, s):
        VowelList = set('aeiouAEIOU')
        s = list(s)
        Left, Right = 0, len(s) - 1 
        
        while Left < Right:
            while Left < Right and s[Left] not in VowelList:
                Left += 1
            while Right > Left and s[Right] not in VowelList:
                Right -= 1
            
            s[Left],s[Right] = s[Right],s[Left]
            Left += 1
            Right -= 1
        
        return "".join(s)