class Solution(object):
    def canVisitAllRooms(self, Rooms):
        Visit  = set()
        Stack = [0]
        while Stack: 
            Room = Stack.pop() 
            Visit.add(Room)
            for Key in Rooms[Room]:
                if Key not in Visit:
                    Stack.append(Key)
        return len(Visit) == len(Rooms)