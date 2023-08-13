class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MorseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        for word in words:
            Morse = ""
            for char in word:
                Morse += MorseCode[ord(char)-97]
            if Morse not in res:
                res.append(Morse)
        return len(res)