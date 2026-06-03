# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columns = defaultdict(list)    # col -> node value
        q = deque([(0, root)])  # (col, node)
        min_col, max_col = 0, 0

        while q:
            col, node = q.popleft()
            columns[col].append(node.val)
            min_col, max_col = min(col, min_col), max(col, max_col)

            if node.left:
                q.append((col - 1, node.left))
            if node.right:
                q.append((col + 1, node.right))

        return [columns[c] for c in range(min_col, max_col + 1)]

    