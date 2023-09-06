class Solution(object):
    def splitListToParts(self, head, k):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        part_size = length // k
        extra = length % k
        result = []
        temp = head
        for i in range(k):
            result.append(temp)
            current_part_size = part_size + 1 if extra > 0 else part_size
            extra -= 1
            for j in range(current_part_size - 1):
                temp = temp.next
            if temp:
                temp.next, temp = None, temp.next
        return result