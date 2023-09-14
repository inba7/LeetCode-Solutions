class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None
        SP = FP = head
        Prev = None
        while FP and FP.next:
            Prev = SP
            SP, FP = SP.next, FP.next.next
        Prev.next = SP.next
        return head