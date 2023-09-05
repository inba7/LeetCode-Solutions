class Solution(object):
    def copyRandomList(self, head):
        Dict = {None:None}
        Curr = head
        while Curr:
            Dict[Curr] = Node(Curr.val)
            Curr = Curr.next
        Curr = head
        while Curr:
            Copy = Dict[Curr]
            Copy.next = Dict[Curr.next]
            Copy.random = Dict[Curr.random]
            Curr = Curr.next
        return Dict[head]
        
        
        return head