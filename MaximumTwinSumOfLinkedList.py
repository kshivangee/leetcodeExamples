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
        #Approach 1: Splitting the two linked list and then reversing the second list and adding the individual elements from the list to get the maximum twin sum value
        newhead = dummy = firstlist = head
        count=0
        while(head):
            head=head.next
            count+=1
        index=0
        while(index!=count//2):
            dummy = dummy.next
            if(index==(count//2 - 1)):
                lastnode=dummy
            index+=1 
        current = lastnode
        prev= nextnode = None
        while(current):
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        secondlist=prev
        maxsum=0
        while(firstlist.next):
            sumlocal = firstlist.val + secondlist.val
            if(sumlocal >maxsum):
                maxsum = sumlocal
            firstlist = firstlist.next
            secondlist = secondlist.next
        return maxsum
    
        #Approach 2: Traversing the linked list and getting the values in a list and performing the list operations to get the maximum twin sum value
        # numlist=[]
        # while(head):
        #     numlist.append(head.val)
        #     head = head.next
        # print(numlist)
        # maxsum=0
        # for i in range(len(numlist)):
        #     if(numlist[i]+numlist[len(numlist)-1-i]>maxsum):
        #         maxsum = numlist[i]+numlist[len(numlist)-1-i]
        # return maxsum




