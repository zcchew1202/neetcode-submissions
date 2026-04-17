class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda i: i[0])
        res = []
        
        # Initialize current interval to track
        curr = intervals[0]
        
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i][0], intervals[i][1]
            cur_start, cur_end = curr[0], curr[1]
            
            if next_start <= cur_end:
                # Overlap: update current interval's end
                curr[1] = max(cur_end, next_end)
            else:
                # No overlap: append finished interval and move to next
                res.append(curr)
                curr = [next_start, next_end]
        
        # Append the last tracked interval
        res.append(curr)
        return res