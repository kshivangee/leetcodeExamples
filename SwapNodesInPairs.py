# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list1=[]
        while head:
            list1.append(head.val)
            head = head.next
        for i in range(1,len(list1),2):
            list1[i], list1[i-1] = list1[i-1], list1[i]
        dummy = newhead = ListNode(0)
        for i in list1:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return newhead.next

