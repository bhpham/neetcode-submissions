class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:  #O(s)
            count = [0] * 26
            for c in s: #O(c)
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())