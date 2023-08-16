# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        Slow, Fast, Prev = head, head, None
        while Fast and Fast.next:
            Fast, Next = Fast.next.next, Slow.next
            Slow.next = Prev
            Prev = Slow
            Slow = Next
        if Fast:
            Slow = Slow.next
        while Prev:
            if Prev.val != Slow.val:
                return False
            Prev, Slow = Prev.next, Slow.next
        return True