class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        compute = ''
        for i in s:
            compute += str(ord(i)-ord('a')+1)
        for i in range(k):
            digitsum=0
            for i in compute:
                digitsum += int(i)
            compute = str(digitsum)
        return int(compute)