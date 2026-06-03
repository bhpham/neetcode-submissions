class TrieNode:

    def __init__(self):
        self.children = {}  #(letter: words)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] 
        cur.isWord = True
    
    def search(self, word):
        def dfs(j, cur):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isWord                    
        
        return dfs(0, self.root)




        
