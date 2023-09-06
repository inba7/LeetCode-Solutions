class Solution(object):
    def splitListToParts(self, head, k):
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        div, mod = divmod(length, k)
        result = []
        node = head
        for _ in range(k):
            result.append(node)
            if not node:
                continue
            part_size = div + 1 if mod > 0 else div
            mod -= 1
            for _ in range(part_size - 1):
                node = node.next
            next_node = node.next
            node.next = None
            node = next_node
        
        return result