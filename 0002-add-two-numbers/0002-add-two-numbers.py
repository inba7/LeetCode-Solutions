# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        Head = ListNode()
        Current = Head
        Carry = 0
        while (l1 != None or l2 != None or Carry != 0):
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            Total = l1_value + l2_value + Carry
            Current.next = ListNode(Total % 10)
            Carry = Total // 10
            # Move list pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            Current = Current.next
        return Head.next