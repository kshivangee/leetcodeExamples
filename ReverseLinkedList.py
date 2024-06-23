# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #Approach 1: Iterate the linked list and using a list operation to reverse the list and convert list into linkedlist
        numslist=[]
        while(head):
            numslist.append(head.val)
            head=head.next
        reversed_list = numslist[::-1]
        # print(reversed_list)
        newhead=current=ListNode(0)
        for i in reversed_list:
            current.next = ListNode(i)
            current = current.next
        return newhead.next


    