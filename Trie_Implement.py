class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):

        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, substr):

        cur = self.root

        for c in substr:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord

    def startsWith(self, start_substr):

        cur = self.root
        for c in start_substr:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True

if __name__ == "__main__":
    t1= Trie()
    t1.insert('apple')
    print(t1.search("appl"))
    print(t1.startsWith('app'))
    
