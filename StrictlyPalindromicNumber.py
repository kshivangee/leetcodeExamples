class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(2,n-1):
            num = []
            number = n
            while(number>0):
                num.append(number%i)
                number = number//i
            if(num!=num[::-1]):
                return False
        return True




        