class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n>0):
            for i in range(2,7):
                while(n%i==0):
                    n=n//i
        return n==1
            
                    
                    
                        