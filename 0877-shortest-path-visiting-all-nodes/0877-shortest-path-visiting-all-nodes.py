class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        target_mask = (1 << n) - 1
        
        memo = [[float('inf')] * (1 << n) for _ in range(n)]
        queue = deque()
        
        for i in range(n):
            queue.append((i, 1 << i, 0))
            memo[i][1 << i] = 0
        
        while queue:
            node, mask, dist = queue.popleft()
            if mask == target_mask:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if dist + 1 < memo[neighbor][new_mask]:
                    memo[neighbor][new_mask] = dist + 1
                    queue.append((neighbor, new_mask, dist + 1))
        return -1