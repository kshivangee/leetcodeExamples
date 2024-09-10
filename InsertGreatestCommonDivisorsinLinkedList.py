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
        #Approach 1: Using List
        list1=[]
        newhead = head
        while(head):
            list1.append(head.val)
            head = head.next
        # print list1
        if(len(list1)==1):
            return newhead
        resultlist = []
        for i in range(len(list1)-1):
            num1= list1[i]
            num2 = list1[i+1]
            result = min(num1,num2)
            while(result):
                if(num1%result == 0 and num2%result==0):
                    break
                result-=1
            resultlist.append(num1)
            resultlist.append(result)
            if(i==len(list1)-2):
                resultlist.append(num2)
        dummy = newhead = ListNode(0)
        for i in resultlist:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return newhead.next
        
        #Approach 2: Using Linked list
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
