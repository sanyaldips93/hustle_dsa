class Solution:
    def solve(self, bt):
        bt.sort()
        waittime = 0
        t = 0
        for i in range(len(bt)):
            waittime += t
            t += bt[i]
        return waittime // len(bt)