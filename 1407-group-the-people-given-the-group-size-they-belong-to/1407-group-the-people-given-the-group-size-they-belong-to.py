class Solution(object):
    def groupThePeople(self, groupSizes):
        group_map = {}
        for i, size in enumerate(groupSizes):
            if size in group_map:
                group_map[size].append(i)
            else:
                group_map[size] = [i]
        result = []
        for size, group in group_map.items():
            for i in range(0, len(group), size):
                result.append(group[i:i+size])
        return result