# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        new_head = head.next
        prev = None
        curr = head
        
        while curr and curr.next:
            next = curr.next
            curr.next = next.next
            next.next = curr
            
            if prev:
                prev.next = next
            
            prev = curr
            curr = curr.next
        
        return new_head