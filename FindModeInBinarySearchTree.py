# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue=[root]
        nodes=[]
        while(queue):
            nodes.append(queue[0].val)
            node = queue.pop(0)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        count, result={},[]
        for i in nodes:
            count[i] = nodes.count(i)
        for i,j in count.items():
            if(j==max(count.values())):
                result.append(i)
        return result



