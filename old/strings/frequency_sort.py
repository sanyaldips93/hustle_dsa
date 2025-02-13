from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        arr = [set() for _ in range(len(s))]
        map = defaultdict(int)

        for ch in s:
            freq = map[ch]
            if freq > 0:
                arr[freq].remove(ch)
            arr[freq+1].add(ch)
            map[ch] += 1
        
        res = ""
        for i in range(len(arr)-1, -1, -1):
            if arr[i]:
                for val in arr[i]:
                    res += (val*i)
        
        return res
    

print(Solution().frequencySort('tree'))