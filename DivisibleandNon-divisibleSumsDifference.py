class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        divisible, nondivisible = [], []
        for i in range(1,n+1):
            if(i%m!=0):
                nondivisible.append(i)
            else:
                divisible.append(i)
        return sum(nondivisible)-sum(divisible)
            
