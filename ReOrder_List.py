# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        list1=[]
        newhead = dummy = head
        while(newhead):
            list1.append(newhead.val)
            newhead=newhead.next
        result=[]
        i,j = 0,len(list1)-1
        index=0
        while(i<=j):
            if(index%2==0):
                index+=1
                result.append(list1[i])
                i+=1
            else:
                index+=1
                result.append(list1[j])
                j-=1
        index=0
        while dummy:
            dummy.val = result[index]
            index+=1
            dummy = dummy.next
        

                
