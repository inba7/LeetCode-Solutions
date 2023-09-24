class Solution(object):
    def minTaps(self, n, R):
        Tap, Count, Best = 0, 0, -1
        while Tap < n:
            Start = max(Tap-100,0)
            End = min(Tap+100,n+1)

            for i in range(Start,Tap):
                if R[i]!= 0 and R[i]+i >= Tap and R[i]+i > Best:
                    Best = R[i] + i
            for i in range(Tap,End):
                if R[i] != 0 and i-R[i] <= Tap and i+R[i] > Best:
                    Best = R[i] + i
            if Best == -1 or Tap == Best:
                return -1
            print(Tap,Best)
            Count += 1
            Tap = Best
        
        return Count