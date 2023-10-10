class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        cand_heap = []

        Left, Right = candidates, n-candidates-1
        
        for i in range(candidates):
            heapq.heappush(cand_heap, (costs[i], i))
        
        for i in reversed(range(n-candidates, n)):
            if i < Left:
                break
            heapq.heappush(cand_heap, (costs[i], i))
        
        Cost = 0
        for _ in range(k):
            cost, inx = heapq.heappop(cand_heap)
            Cost += cost
            if Left <= Right: 
                if inx < Left:
                    heapq.heappush(cand_heap, (costs[Left], Left))
                    Left += 1
                elif inx > Right:
                    heapq.heappush(cand_heap, (costs[Right], Right))
                    Right -= 1
        return Cost 