class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            startA, startB = firstList[i][0], secondList[j][0]
            endA, endB = firstList[i][1], secondList[j][1]

            start = max(startA, startB)
            end = min(endA, endB)

            if start <= end:
                res.append([start, end])
            
            if endA < endB:
                i += 1
            else:
                j += 1
        
        return res