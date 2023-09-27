class Solution(object):
    def decodeAtIndex(self, S, K):
        A = [1]
        for x in S[1:]:
            if A[-1] >= K : 
                break
            if x.isdigit():
                A.append( A[-1]*int(x) )
            else:
                A.append( A[-1]+1 )
        for i in reversed(range(len(A))):
            K %= A[i]
            if not K and S[i].isalpha():
                return S[i]