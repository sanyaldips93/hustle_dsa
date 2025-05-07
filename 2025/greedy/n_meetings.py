class Solution:
    def maximumMeetings(self,start,end):
        
        arr = [[start[i], end[i]] for i in range(len(start))]
        arr.sort(key=lambda x: (x[1], x[0]))
        last = arr[0]
        res = 1
        for i in range(1, len(end)):
            if arr[i][0] > last[1]:
                res += 1
                last = arr[i]
        
        return res