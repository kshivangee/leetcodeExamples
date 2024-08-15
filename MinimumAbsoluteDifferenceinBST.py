import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        treenodes = []
        queue = [root]
        while(queue):
            treenodes.append(queue[0].val)
            node = queue.pop(0)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        mindiff = sys.maxint
        for i in range(len(treenodes)):
            for j in range(i+1, len(treenodes)):
                if(abs(treenodes[i]-treenodes[j])<mindiff):
                    mindiff = abs(treenodes[i]-treenodes[j])
        return mindiff