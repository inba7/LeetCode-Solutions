class Solution(object):
    def winnerOfGame(self, colors):
        Alice, Bob = 0, 0

        for i in range(1, len(colors) - 1):
            Current = colors[i]
            Prev = colors[i-1]
            Next = colors[i+1]

            if Current == 'A' and Prev == 'A' and Next == 'A':
                Alice += 1 
            elif Current == 'B' and Prev == 'B' and Next == 'B':
                Bob += 1  
                
        return Alice > Bob