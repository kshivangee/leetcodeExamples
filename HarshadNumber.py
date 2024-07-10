class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        newn = x
        sumdigits = 0
        while(newn>0):
            digit = newn % 10
            sumdigits += digit
            newn = newn//10
        if(x%sumdigits==0):
            return sumdigits
        else:
            return -1


