'''
order = "xabcfg"
s = "bdca"


Approach: Using HashMap
count = {
    b: 0
    d: 1
    c: 0
    a: 0
}

result =  "abcd"

'''
#TC: O(S + O) where S is the length of string s, and O is length of Order
#SC: O(26) it can go up only to 26 lowercase English characters
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0] * 26
        res = []

        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for c in order:
            res.append(c * count[ord(c) - ord('a')])
            count[ord(c) - ord('a')] = 0

        for c, n in enumerate(count):
            res.append(chr(c + ord('a')) * n)
        
        return "".join(res)