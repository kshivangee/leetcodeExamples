class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count=s.count(s[0])
        for i in s:
            if(s.count(i)==count):
                continue
            else:
                return False
        return True
