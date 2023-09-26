class Solution(object):
    def travel(self, city, mp, visited):
        n = len(mp)
        for next_city in range(n):
            if next_city not in visited and mp[city][next_city] == 1:
                visited.add(next_city)
                self.travel(next_city, mp, visited)

    def findCircleNum(self, isConnected):
        n = len(isConnected)

        visited = set([])
        group = 0
        for city in range(n):
            if not (city in visited):
                visited.add(city)
                group += 1
                self.travel(city, isConnected, visited)
        return group