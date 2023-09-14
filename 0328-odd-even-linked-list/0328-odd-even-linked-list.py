class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd_head, even_head = head, head.next
        odd_ptr, even_ptr = odd_head, even_head
        current = even_head.next
        is_odd = True

        while current:
            if is_odd:
                odd_ptr.next = current
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = current
                even_ptr = even_ptr.next
            current = current.next
            is_odd = not is_odd

        odd_ptr.next = None
        even_ptr.next = None
        odd_ptr.next = even_head

        return odd_head