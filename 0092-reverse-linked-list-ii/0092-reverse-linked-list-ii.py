class Solution(object):
    def reverseBetween(self, head, left, right):
        Dummy = ListNode(0,head)
        K = right-left+1
        Prev, i = None, 1
        Curr = Dummy.next
        PrevCur = Dummy
        while i<left:
            PrevCur = PrevCur.next
            Curr = Curr.next
            i+=1
        NewTail = PrevCur.next
        Count = 0
        while K:
            next = Curr.next
            Curr.next = Prev
            Prev = Curr
            Curr = next
            K-=1
        PrevCur.next = Prev
        NewTail.next = Curr
        return Dummy.next