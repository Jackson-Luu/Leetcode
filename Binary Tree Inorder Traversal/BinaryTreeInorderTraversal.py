# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        if root.left == None and root.right == None: 
            return [root.val]
        
        if root.left != None:
            path = self.inorderTraversal(root.left)
            path.append(root.val)
        else:
            path = [root.val]
        if root.right != None:
            path.extend(self.inorderTraversal(root.right))
        return path
