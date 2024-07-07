# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        index=0
        newhead = list1
        newhead2 = list2
        remlist1, prev=None, None
        while(list1):
            if(index==(a-1)):
                prev = list1
            if(index==a or index==b):
                if(index==a and index==b):
                    remlist1= list1.next
                    index+=1
                if(index==a):
                    list1=list1.next
                    index+=1
                if(index==b):
                    remlist1= list1.next
                    index+=1
            if(index!=a):
                list1=list1.next
                index+=1
    
        while(list2.next):
            list2=list2.next
        list2.next = remlist1
        prev.next = newhead2
        return newhead