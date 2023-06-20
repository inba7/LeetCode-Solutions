# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return head
        
        current = head
        previous = None
        
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        return previous