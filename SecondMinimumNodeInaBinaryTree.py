# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minimum = []
        queue = [root]
        while(queue):
            minimum.append(queue[0].val)
            node = queue.pop(0)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        minimum = list(set(minimum))
        minimum.sort()
        print minimum
        if(len(minimum)>1):
            return minimum[1]
        else:
            return -1


        