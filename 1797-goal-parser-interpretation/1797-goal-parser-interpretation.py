class Solution(object):
    def interpret(self, command):
        command = command.replace("()", "o")
        return command.replace("(al)", "al")