# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def inOrder(self,root):
#     result=[]
#     if(root):
#         self.inOrder(root.left)
#         result.append(root.val)
#         print result
#         self.inOrder(root.right)
#     return result

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        result=[]
        def inOrder(root):
            if(root):
                inOrder(root.left)
                result.append(root.val)
                inOrder(root.right)
            return result
       
        newroot = dummy = root
        inorder_list = inOrder(newroot)
        print(inorder_list)
        queue = [dummy]
        while(queue):
            value = queue[0].val
            index = inorder_list.index(value)
            newvalue = value + sum(inorder_list[index+1:])
            queue[0].val = newvalue
            node = queue.pop(0)
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        return root

        