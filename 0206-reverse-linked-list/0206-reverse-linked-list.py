# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        Prv, Cur = None, head

        while Cur:
            next = Cur.next
            Cur.next = Prv
            Prv = Cur
            Cur = next
        return Prv