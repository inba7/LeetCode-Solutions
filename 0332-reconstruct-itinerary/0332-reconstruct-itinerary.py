import collections
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        ans = []
        graph = collections.defaultdict(list)
        for a, b in tickets:
            graph[a].append(b)
        for u in graph:
            heapq.heapify(graph[u])
        def dfs(u):
            while u in graph and graph[u]:
                dfs(heapq.heappop(graph[u]))
            ans.append(u)
        dfs('JFK')
        return ans[::-1]