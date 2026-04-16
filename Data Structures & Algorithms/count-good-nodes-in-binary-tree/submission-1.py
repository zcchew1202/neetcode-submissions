# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, maxVal):
        # nodes 1 is no good, 2 is in the way > 1
        # same for the other ones
        if not root:
            return 0
        # do a dfs on each node starting from root
        # 2 is good bc no other node is > 2
        # track max val of node when dfs
        # if cur val of node >= maxVal then it's good
        count = 1 if root.val >= maxVal else 0
        maxVal = max(maxVal,root.val)
        count += self.dfs(root.left, maxVal)
        count += self.dfs(root.right, maxVal)
        return count
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

        

        
            
        
        