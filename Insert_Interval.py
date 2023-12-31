class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while( i<len(intervals) and intervals[i][0] < newInterval[0]):
            i+= 1
        
        intervals.insert(i,newInterval)
        
        ans = []
        for interval in intervals:
            if len(ans) == 0 or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
        