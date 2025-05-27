from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(i, cur):
            if i == len(digits):
                res.append(cur)
                return
            for ch in digitToChar[digits[i]]:
                dfs(i+1, cur+ch)
        dfs(0, "") if digits else None
        return res