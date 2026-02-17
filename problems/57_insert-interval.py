class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

s = Solution()

print("Example 1:")
print("Input: [[1,3],[6,9]], newInterval = [2,5]")
print("Output:", s.insert([[1,3],[6,9]], [2,5]))
print()

print("Example 2:")
print("Input: [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]")
print("Output:", s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
