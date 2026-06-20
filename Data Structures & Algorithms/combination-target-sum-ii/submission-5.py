''''
candidates = [9,2,2,4,6,1,5] , target = 8

            9 2 2 2 4 6 1 5
        Sorting -> 1,  2, 2, 2, 4, 5, 6, 9
                                


res = [1, 2, 5], [2, 2, 4], [2, 6]

'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return res
            if i == len(candidates) or total > target:
                return

            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()

            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, cur, total)
            
        backtrack(0, [], 0)
        return res

