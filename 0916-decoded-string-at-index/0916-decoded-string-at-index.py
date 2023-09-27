class Solution(object):
    def decodeAtIndex(self, s, k):
        decoded_length = 0  

        for char in s:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1

        for i in range(len(s) - 1, -1, -1):
            current_char = s[i]
            if current_char.isdigit():
                decoded_length //= int(current_char)
                k %= decoded_length
            else:
                if k == 0 or decoded_length == k:
                    return current_char
                decoded_length -= 1
        return ""