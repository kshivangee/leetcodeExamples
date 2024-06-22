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
        #Approach 1: By iterating the linkedlist for getting the last node and counting the elements. Then iterating the linked list and pushing all the odd nodes after the last node
        newhead = current = head
        count=0
        while(newhead):
            if(newhead.next ==None):
                lastNode = newhead
            count+=1
            newhead = newhead.next
        if(count==0):
            return None
        index = 0
        while(index != count):
            if(index%2==0):
                prev = current
            if(index%2!=0):
                lastNode.next = ListNode(current.val)
                prev.next = current.next
                lastNode = lastNode.next  
            index+=1      
            current = current.next
        return head

        #Approach 2: By iterating the linkedlist and getting the list. By performing list slicing to push the odd elements at the end of the list and then creating a linkedlist from the modified list
        # numlist = []
        # while(head):
        #     numlist.append(head.val)
        #     head = head.next
        # newnumlist = numlist[0::2]+numlist[1::2]
        # newhead = head = ListNode(0)
        # for i in newnumlist:
        #     newhead.next = ListNode(i)
        #     newhead = newhead.next
        # return head.next
        
