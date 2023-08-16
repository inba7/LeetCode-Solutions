# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        Slow, Fast, Prev = head, head, None
        while Fast and Fast.next:
            Slow, Fast = Slow.next, Fast.next.next
        Prev, Slow, Prev.next = Slow, Slow.next, None
        while Slow:
            Slow.next, Prev, Slow = Prev, Slow, Slow.next
        Fast, Slow = head, Prev
        while Slow:
            if Fast.val != Slow.val: return False
            Fast, Slow = Fast.next, Slow.next
        return True