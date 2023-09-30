class Solution(object):
    def find132pattern(self, nums):
        Length = len(nums)
        if Length < 3:
            return False
        Stack = deque()
        Max3 = float('-inf')

        for i in range(Length - 1, -1, -1):
            Current = nums[i]
            if Current < Max3:
                return True
            while Stack and Stack[0] < Current:
                Max3 = Stack.popleft()
            Stack.appendleft(Current)
        return False