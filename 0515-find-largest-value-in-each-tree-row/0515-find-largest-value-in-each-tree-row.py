from collections import deque

class Solution:
    def largestValues(self, root):
        if not root:
            return []
        Queue = deque([(root, 0)])
        Dict = {0:root.val}
        
        while Queue:
            Curr, Row = Queue.popleft()
            for Child in [Curr.left, Curr.right]:
                if Child:
                    Queue.append([Child, Row+1])
                    if Row+1 not in Dict: Dict[Row+1] = Child.val
                    else: Dict[Row+1] = max(Child.val, Dict[Row+1])
        
        Res = []
        for Key in range(len(Dict.keys())):
            Res.append(Dict[Key])
        return Res