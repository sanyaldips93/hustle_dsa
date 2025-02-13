from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            idx1 = D.popleft()
            idx2 = R.popleft()
            if idx1 < idx2:
                D.append(idx1 + len(senate))
            else:
                R.append(idx2 + len(senate))
        
        return "Radiant" if R else "Dire"