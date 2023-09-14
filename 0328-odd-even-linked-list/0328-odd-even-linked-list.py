class Solution(object):
    def oddEvenList(self, head):
        if head:
            odd = head
            even = head.next
            even_head = even
        else:
            return

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head