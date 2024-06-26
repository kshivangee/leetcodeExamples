class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        result=''
        x= len(str1)
        y = len(str2)
        while y:
            x,y = y, x%y
        gcd_length = x
        result = str1[:gcd_length]
        str1count = str1.count(result)
        str2count = str2.count(result)

        if(set(str1)==set(result) and set(str2)==set(result) and str1count==(len(str1)//len(result)) and str2count==(len(str2)//len(result))):
            return str1[:gcd_length]
        else:
            return ''
