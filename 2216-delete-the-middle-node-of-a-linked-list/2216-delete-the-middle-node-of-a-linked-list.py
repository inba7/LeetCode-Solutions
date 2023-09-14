class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None
        Prev, SP, FP = None, head, head
        while FP and FP.next:
            Prev = SP
            SP, FP = SP.next, FP.next.next
        Prev.next = SP.next
        return head