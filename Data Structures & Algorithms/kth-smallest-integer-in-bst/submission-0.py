# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        count = 0
        def dfs(root, k):
            nonlocal count, res
            if not root:
                return
            dfs(root.left, k)
            count += 1
            if count == k:
                res = root.val
                print("res", res)
                return
            dfs(root.right, k)
        dfs(root, k)
        return res