'''
cat -> bat -> bag -> sag
-> 4
pattern: ca*
sag
'''

class Solution:
    #TC: O(w * l * log(n)) where w is number of words in wordList, l is number of characters of each word, n is number words on push/pop from queue
    #SC: O(n) where n is auxiliary space of using extra dsa with hashMap, hashSet, and Queue
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add((neiWord))
                            q.append((neiWord))
            res += 1
        
        return 0


