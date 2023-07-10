class Solution(object):
    def longestCommonPrefix(self, strs):
        answer = ""
        i=0
        shorted_word = len(min(strs, key=len))
        while i < shorted_word:
            target_letter = strs[0][i]
            for word in strs:
                word_in = word[i]
                if target_letter != word_in:
                    return answer
            i+=1
            answer+=target_letter    
        return answer