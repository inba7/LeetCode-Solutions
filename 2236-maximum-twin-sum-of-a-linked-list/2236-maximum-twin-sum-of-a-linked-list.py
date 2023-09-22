class Solution(object):
    def pairSum(self, head):
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        i = 0
        r = len(l)-1
        max_sum = 0
        while(i<r):
            max_sum = max(l[i]+l[r],max_sum)
            i+=1
            r-=1
        return max_sum 