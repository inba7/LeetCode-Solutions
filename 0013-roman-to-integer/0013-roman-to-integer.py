class Solution(object):
    def romanToInt(self, s):
        sum = 0
        index=0
        dict1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        dict2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        liste=[]
        for i in s:
            liste.append(i)
        
        while len(liste) > index:
            if index < len(liste) - 1 and liste[index] + liste[index+1] in dict2:
                value = dict2[liste[index] + liste[index+1]]
                sum += value
                index += 2
            else:
                value=dict1[liste[index]]
                sum+=value
                index += 1
        
        return sum