class Node:
    def __init__(self):
        self.children = {}
        self.endsWith = 0
        self.countPrefix = 0

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            cur.endsWith += 1
            cur.countPrefix += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.children: return 0
            cur = cur.children[c]
        return cur.endsWith

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children: return 0
            cur = cur.children[c]
        return cur.countPrefix
    
    def erase(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children: return False
            cur = cur.children[c]
            cur.endsWith -= 1
            cur.countPrefix -= 1
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("apple")
print(obj.countWordsEqualTo("apple"))
print(obj.countWordsStartingWith("apple"))
print(obj.erase('apple'))
print(obj.countWordsEqualTo("apple"))
print(obj.countWordsStartingWith("apple"))
print(obj.countWordsEqualTo("apps"))
print(obj.countWordsStartingWith("apps"))
print(obj.erase('apps'))