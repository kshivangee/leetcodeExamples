# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root is None):
            return 0
        else:
            queue=[]
            height=0
            queue.append(root)
            while(queue):
                count = len(queue)
                while(count>0):
                    node = queue.pop(0)
                    if(node.left):
                        queue.append(node.left)
                    if(node.right):
                        queue.append(node.right)
                    count-=1
                height+=1
            return height

