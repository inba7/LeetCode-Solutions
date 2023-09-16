class Solution(object):
    def canVisitAllRooms(self, rooms):
        keys, visited = rooms[0], {0}
        while keys:
            r = keys.pop(0)
            visited.add(r)
            for k in rooms[r]:
                if k not in visited:
                    keys.append(k)
        return len(visited)==len(rooms)