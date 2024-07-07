# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(head is None):
            return None
        if(head.next is None):
            return head
        newhead = head
        while(newhead.next):
            gcd=0
            current = newhead
            num1 = newhead.val
            num2= newhead.next.val
            newhead=newhead.next
            for i in range(1, max(num1, num2)+1):
                if(num1%i==0 and num2%i==0):
                    if(i>gcd):
                        gcd = i
            # print num1, num2,gcd
            newNode = ListNode(gcd)
            current.next = newNode
            current = current.next
            newNode.next = newhead
        return head
            

        