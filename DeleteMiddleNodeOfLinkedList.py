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
        # Approach 1: Traversing the linked list by counting the elements in a list and then deleting middle element 
        count = 0
        newhead = head
        while(newhead):
            count+=1
            newhead=newhead.next
        middle = count//2
        if(middle == 0):
            return None
        index = 0
        newhead = head
        while(newhead):
            if(index == middle-1):
                newhead.next = newhead.next.next
            newhead = newhead.next
            index+=1
        return head 


        # Approach 2: Traversing the linked list by appending the elements in a list and then deleting middle element from the list and converting list to linkedlist
        # numlist=[]
        # while(head):
        #     numlist.append(head.val)
        #     head=head.next
        # del numlist[len(numlist)//2]
        # newhead = currentnode = ListNode(0)
        # for i in numlist:
        #     currentnode.next = ListNode(i)
        #     currentnode = currentnode.next
        # return newhead.next
