# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        count = 1

        count += max(self.dfs(node.left),self.dfs(node.right))
        return count


        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root)