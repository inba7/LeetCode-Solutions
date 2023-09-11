class Solution(object):
    def countKDifference(self, nums, k):
        Dict = {}
        for i in nums:
            if i in Dict:
                Dict[i]+=1
            else:
                Dict[i]=1
        Pairs = 0
        for i in nums:
            Diff = (i-k)
            if Diff in Dict:
                Pairs += Dict[Diff]
        return Pairs