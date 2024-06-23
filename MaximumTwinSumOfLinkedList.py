# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        #Approach 1: Iterate the linked list and using a list operation to calculate the twinsum of the elements and return it
        numlist=[]
        while(head):
            numlist.append(head.val)
            head = head.next
        print(numlist)
        maxsum=0
        for i in range(len(numlist)):
            if(numlist[i]+numlist[len(numlist)-1-i]>maxsum):
                maxsum = numlist[i]+numlist[len(numlist)-1-i]
        return maxsum




