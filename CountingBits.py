class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result=[]
        for i in range(n+1):
            binary = list(bin(i).replace('0b',''))
            total = [int(i) for i in binary]
            result.append(sum(total))
        return result