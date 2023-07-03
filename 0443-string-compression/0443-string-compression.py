class Solution(object):
    def compress(self, chars):
        writer = 0
        begin = 0
        while begin < len(chars):
            end = begin
            while end + 1 < len(chars) and chars[end + 1] == chars[end]:
                end += 1
            chars[writer] = chars[begin]
            writer += 1
            if end > begin:
                count = str(end - begin + 1)
                for c in count:
                    chars[writer] = c
                    writer += 1
            begin = end + 1
        return writer