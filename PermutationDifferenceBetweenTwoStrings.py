class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        result=0
        for i in s:
            result+= abs(s.index(i)-t.index(i))
        return result
