class Solution:
    def isMatch(self, s, p):
        self.cache = {}
        def isM(s,p):
            if (s,p) in self.cache:
                return self.cache[(s,p)]
            
            if not p:
                return not s

            if p[-1] == "*" and isM(s,p[:-2]):
                self.cache[(s,p)] = True
                return True
                
            if p[-1] == "*" and s and (s[-1] == p[-2] or p[-2] == '.') and isM(s[:-1], p):
                    self.cache[(s, p)] = True
                    return True    

            if s and (p[-1] == s[-1] or p[-1] == '.') and isM(s[:-1], p[:-1]):
                self.cache[(s, p)] = True
                return True
            
            self.cache[(s, p)] = False
            return False
        
        return isM(s,p)