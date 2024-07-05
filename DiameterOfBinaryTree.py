# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        self.height(root)
        return self.ans

    def height(self, root):
        if(root is None):
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        print lheight, rheight, root.val
        self.ans = max(self.ans, lheight+rheight)
        return max(lheight, rheight)+1