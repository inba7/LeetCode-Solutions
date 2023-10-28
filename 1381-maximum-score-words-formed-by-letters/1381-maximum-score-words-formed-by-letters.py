from string import ascii_lowercase
class Solution(object):
    results = {}
    score = []
    def maxScoreWords(self, words, letters, score):
        self.results.clear()
        self.score = score
        letter_count = {}
        for index, char in enumerate(ascii_lowercase):
            letter_count[index] = letters.count(char)
        
        return self.max_score(words, letter_count)

    def max_score(self, words, letter_count):
        if len(words) == 0:
            return 0
        curr_score = 0
        new_letter_count = letter_count.copy()
        for char in words[0]:
            new_letter_count[ascii_lowercase.index(char)] -= 1
            if new_letter_count[ascii_lowercase.index(char)] < 0:
                curr_score = -1
                break
            else:
                curr_score += self.score[ascii_lowercase.index(char)]
        if curr_score == -1:
            return self.max_score(words[1:], letter_count)
        else:
            return max(curr_score + self.max_score(words[1:], new_letter_count),  self.max_score(words[1:], letter_count))