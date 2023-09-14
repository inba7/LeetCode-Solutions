class Solution(object):
    def decodeString(self, s):
        Output = []
        for n in range(len(s)):
            if s[n] != "]":
                Output.append(s[n])
            else:
                SubStr = ""
                while Output[-1] != "[":
                    SubStr = Output.pop() + SubStr
                Output.pop()
                Freq = ""
                while Output and Output[-1].isdigit():
                    Freq = Output.pop() + Freq
                Output.append(int(Freq) * SubStr)
        return "".join(Output)