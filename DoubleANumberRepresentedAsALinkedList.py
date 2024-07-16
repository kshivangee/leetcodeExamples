# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        str1=""
        while(head):
            str1+= str(head.val)
            head = head.next
        print str1
        double = str(int(str1)*2)
        list1 = [num for num in double]
        head = dummy = ListNode(0)
        for i in list1:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return head.next