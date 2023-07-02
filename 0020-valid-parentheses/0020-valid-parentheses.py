class Solution(object):
    def isValid(self, s):
        stack = deque()
        for char in s:
            if char == "{":
                stack.append("}")
            elif char == "(":
                stack.append(")")
            elif char == "[":
                stack.append("]")
            elif len(stack) == 0 or stack.pop() != char: 
                return False
        if len(stack) == 0: return True
        return False