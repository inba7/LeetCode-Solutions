class Solution(object):
    def minimumTime(self, n, relations, time):
        Graph = [[] for _ in range(n)]
        for Prev, Next in relations:
            Graph[Prev-1].append(Next - 1)
        Memo = [-1] * n

        def calculateTime(Course):
            if Memo[Course] != -1:
                return Memo[Course]
            if not Graph[Course]:
                Memo[Course] = time[Course]
                return Memo[Course]

            MaxPrerequisite = 0
            for prereq in Graph[Course]:
                MaxPrerequisite = max(MaxPrerequisite, calculateTime(prereq))
            Memo[Course] = MaxPrerequisite + time[Course]
            return Memo[Course]

        OverallMin = 0
        for Course in range(n):
            OverallMin = max(OverallMin, calculateTime(Course))
        return OverallMin