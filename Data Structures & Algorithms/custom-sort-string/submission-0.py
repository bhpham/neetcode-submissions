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
        count = {}
        res = []

        for c in s:
            count[c] = 1 + count.get(c, 0)
        
        for c in order:
            if c in count:
                res.append(c * count[c])
                count[c] = 0
        
        for letter, freq in count.items():
            res.append(letter * freq)
        
        return "".join(res)


 