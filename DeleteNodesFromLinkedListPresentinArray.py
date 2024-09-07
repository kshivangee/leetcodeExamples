# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1=[]
        numset = set(nums)
        while(head):
            list1.append(head.val)
            head = head.next
        dummy = newhead = ListNode(0)
        for i in range(len(list1)):
            if(list1[i] not in numset):
                dummy.next = ListNode(list1[i])
                dummy = dummy.next
            
        return newhead.next
            