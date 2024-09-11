class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        list1= [i for i in range(1,n+1)]
        for i in range(len(list1)):
            if(sum(list1[:i])==sum(list1[i+1:])):
                return list1[i]
        else:
            return -1