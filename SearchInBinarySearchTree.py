# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # while(root):
        #     if(root.val==val):
        #         return root
        #     else:
        #         if(val<root.val):
        #             root=root.left
        #         else:
        #             root=root.right
        # return root

        #Traverse the tree using the Level Order Traversal and if found print the subtree
        queue = []
        queue.append(root)
        while(len(queue)>0):
            if(queue[0].val==val):
                return queue[0]
            node = queue.pop(0)
            if(node.left != None):
                queue.append(node.left)
            if(node.right != None):
                queue.append(node.right)
        else:
            return None
