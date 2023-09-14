class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None
        Prev, SP, FP = None, head, head
        while True:
            if FP.next and FP.next.next:
                Prev, SP, FP = SP, SP.next, FP.next.next
                continue
            if FP.next:
                SP.next = SP.next.next
            else:
                Prev.next = SP.next
            break
        return head