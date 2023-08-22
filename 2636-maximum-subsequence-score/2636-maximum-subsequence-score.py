class Solution(object):
    def maxScore(self, nums1, nums2, k):
        Total, Max = 0, 0
        Heap = []
        for x, y in sorted(list(zip(nums1, nums2)), key=lambda xy: -xy[1]):
            heappush(Heap, x)
            Total += x
            if len(Heap) > k:
                Total -= heappop(Heap)
            if len(Heap) == k:
                Max = max(Max, Total * y)
        return Max