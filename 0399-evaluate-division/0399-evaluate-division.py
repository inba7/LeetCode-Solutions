class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        for (x,y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0/val

        def dfs(src, target, visited):
            if src not in graph or target not in graph:
                return -1.0
            if src == target:
                return 1.0
            visited.add(src)
            for neighbor, val in graph[src].items():
                if neighbor in visited:
                    continue
                ret_val = dfs(neighbor,target, visited)
                if ret_val != -1.0:
                    return val * ret_val
            return -1.0
        
        result = []
        for c,d in queries:
            result.append(dfs(c,d,set()))
        return result