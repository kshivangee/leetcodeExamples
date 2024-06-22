# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        numlist=[]
        while(head):
            numlist.append(head.val)
            head=head.next
        del numlist[len(numlist)//2]
        newhead = currentnode = ListNode(0)
        for i in numlist:
            currentnode.next = ListNode(i)
            currentnode = currentnode.next
        return newhead.next