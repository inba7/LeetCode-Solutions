class Solution(object):
    def canVisitAllRooms(self, Rooms):
        Seen = [False] * len(Rooms)
        Seen[0] = True
        Q = deque([0])
        while Q:
            Node = Q.popleft()
            for Room in Rooms[Node]:
                if not Seen[Room]:
                    Seen[Room] = True
                    Q.append(Room)
        return all(Seen)