# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        numlist = []
        while(head):
            numlist.append(head.val)
            head = head.next
        newnumlist = numlist[0::2]+numlist[1::2]
        newhead = head = ListNode(0)
        for i in newnumlist:
            newhead.next = ListNode(i)
            newhead = newhead.next
        return head.next
        