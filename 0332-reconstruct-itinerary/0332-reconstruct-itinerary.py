class Solution(object):
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for from_loc, to_loc in tickets:
            graph[from_loc].append(to_loc)
        for from_loc in graph:
            graph[from_loc].sort(reverse=True)
        self.ans = []
        self.dfs(graph, "JFK")
        return self.ans[::-1]
    
    def dfs(self, graph, root):
        while graph[root]:
            self.dfs(graph, graph[root].pop())
        self.ans.append(root)