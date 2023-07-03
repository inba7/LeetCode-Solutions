class Solution(object):
    def compress(self, chars):
        ans, i = 0,0
        while i < len(chars):
            l = chars[i]
            c = 0
            while i < len(chars) and chars[i] == l:
                c += 1
                i += 1
            chars[ans] = l
            ans += 1
            if c > 1:
                for c in str(c):
                    chars[ans] = c
                    ans += 1          
        return ans