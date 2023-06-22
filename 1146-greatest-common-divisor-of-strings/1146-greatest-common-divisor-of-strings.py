class Solution(object):
    def gcdOfStrings(self, str1, str2):
        temp_str = ''
        if len(str2)> len(str1):
            str1,str2= str2,str1
        for i in range(len(str2),0,-1):
            temp_str = str2[:i]

            if temp_str * (len(str1)//len(temp_str)) == str1 and temp_str * (len(str2)//len(temp_str)) == str2:
                return temp_str
        return ''