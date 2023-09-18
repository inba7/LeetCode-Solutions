class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        s = s.lower()
        start = 0 
        end = len(s)-1

        while start < end:
            if s[start] != s[end]:
                return False

            start = start + 1
            end = end -1
            
        return True