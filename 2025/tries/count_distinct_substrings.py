class Node:
    def __init__(self):
        self.children = {}


def countDistinctSubstring(s):
    root = Node()
    res = 0
    for i in range(len(s)):
        cur = root
        for ch in s[i:]:
            if ch not in cur.children:
                cur.children[ch] = Node()
                res += 1
            cur = cur.children[ch]
    return res + 1


def countDistinctSubstring2(s):
    root = {}
    res = 0
    for i in range(len(s)):
        cur = root
        for ch in s[i:]:
            if ch not in cur:
                cur[ch] = {}
                res += 1
            cur = cur[ch]
    return res + 1


print(countDistinctSubstring('abab'))