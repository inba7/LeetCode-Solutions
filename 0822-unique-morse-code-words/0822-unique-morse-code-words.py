class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MorseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            Morse = ""
            for char in word:
                Morse += MorseCode[ord(char)-97]
            res.add(Morse)
        return len(res)