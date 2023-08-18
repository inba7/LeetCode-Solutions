class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        Dummy = ListNode(0)
        Cur = Dummy
        Carry = 0
        while l1 or l2:
            Sum = Carry
            if l1:
                Sum += l1.val
                l1 = l1.next
            if l2:
                Sum += l2.val
                l2 = l2.next
            Carry = Sum // 10
            Cur.next = ListNode(Sum % 10)
            Cur = Cur.next
        if Carry:
            Cur.next = ListNode(Carry) 
        return Dummy.next