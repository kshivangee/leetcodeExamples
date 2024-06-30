class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0):
            return 0
        if(n==1 or n==2):
            return 1
        else:
            F=[0]*(n+1)      
            F[0]=0
            F[1]=F[2]=1
            for i in range(n-2):
                F[i+3] = F[i]+F[i+1]+F[i+2]
            return F[n]
       