# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        list1=[]
        result=0
        while(head!=None):
            list1.append(head.val)
            head = head.next
        index=0
        for i in range(len(list1)-1,-1,-1):
            result += list1[i]*pow(2,index)
            index+=1
        return result
