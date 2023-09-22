class Solution(object):
    def pairSum(self, head):
        Slow, Fast = head, head
        Prev = None
        while (Fast and Fast.next):
            Fast = Fast.next.next
            Temp = Slow.next
            Slow.next = Prev
            Prev = Slow
            Slow = Temp
        Res = 0
        while Slow:
            Res = max(Res, Prev.val + Slow.val)
            Prev = Prev.next
            Slow = Slow.next
        return Res