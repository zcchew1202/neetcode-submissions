# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        indices = {val: i for i, val in enumerate(inorder)}
        # A global variable tracks the current index in the pre-order array
        self.pre_idx = 0
        #Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
        #Output: [1,2,3,null,null,null,4]
        def dfs(l,r):
            if l > r:
                return None
            rootVal = preorder[self.pre_idx]
            root = TreeNode(rootVal)
            mid = indices[rootVal]
            self.pre_idx += 1
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0,len(inorder)-1)
        


