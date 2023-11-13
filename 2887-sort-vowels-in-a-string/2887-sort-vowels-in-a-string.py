class Solution(object):
    def sortVowels(self, s):
        Vowels, VowelPosx = [], []
        
        for Idx, Char in enumerate(s):
            if Char.lower() in 'aeiou':
                Vowels.append(Char)
                VowelPosx.append(Idx)
        
        Vowels.sort()
        Result = list(s)
        for Pos, Vowel in zip(VowelPosx, Vowels):
            Result[Pos] = Vowel
        
        return ''.join(Result)