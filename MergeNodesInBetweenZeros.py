# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #Approach 1: Using Linked list
        sumNodes=0
        modify = head
        traverse = head.next
        while(traverse):
            if(traverse.val!=0):
                sumNodes += traverse.val
                traverse=traverse.next
                print sumNodes
            else:
                modify.val=sumNodes
                sumNodes=0
                modify.next = traverse
                if(traverse.next!=None):
                    modify = traverse
                traverse=traverse.next
        modify.next=None
        return head


        #Approach 2: Using list operations
        # newlist=[]
        # while(head):
        #     newlist.append(head.val)
        #     head = head.next
        # # print newlist
        
        # result=[]
        # sumnodes=0
        # for i in range(len(newlist)):
        #     if(i!=0 and newlist[i]==0):
        #         result.append(sumnodes)
        #         sumnodes=0
        #     else:
        #         sumnodes+=newlist[i]
        # # print result
        # newhead = dummy = ListNode(0)
        # for i in result:
        #     dummy.next = ListNode(i)
        #     dummy = dummy.next
        # return newhead.next



            

        