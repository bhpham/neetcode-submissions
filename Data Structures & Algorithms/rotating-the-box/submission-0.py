class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])

        for r in range(ROWS):
            i = COLS - 1
            for c in reversed(range(COLS)):
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i -= 1
                elif boxGrid[r][c] == "*":
                    i = c - 1
        
        res = []

        for c in range(COLS):
            col = []
            for r in reversed(range(ROWS)):
                col.append(boxGrid[r][c])
            res.append(col)


        return res