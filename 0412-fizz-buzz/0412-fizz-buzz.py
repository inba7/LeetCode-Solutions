class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for Inc in range(1,n+1):
            if (Inc%3==0 and Inc%5==0):
                answer.append("FizzBuzz")
            elif (Inc%3==0):
                answer.append("Fizz")
            elif (Inc%5==0):
                answer.append("Buzz")
            else:
                answer.append(str(Inc))
        return answer