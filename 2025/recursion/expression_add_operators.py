from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def backtrack(i, path, last, val):
            if i == len(num):
                if val == target:
                    res.append(path)
                return

            for j in range(i, len(num)):
                if j != i and num[i] == '0':
                    break
                curstr = num[i:j+1]
                curnum = int(curstr)
                if i == 0:
                    backtrack(j+1, curstr, curnum, curnum)
                else:
                    backtrack(j+1, path+"+"+curstr, curnum, val+curnum) # "+"
                    backtrack(j+1, path+"-"+curstr, -curnum, val-curnum) # "-"
                    backtrack(j+1, path+"*"+curstr, last*curnum, val-last+last*curnum) # "*"
        
        backtrack(0, "", 0, 0)
        return res
    
print(Solution().addOperators("232", 8))