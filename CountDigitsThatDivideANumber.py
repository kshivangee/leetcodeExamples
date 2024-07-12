class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        newnum=num
        while(num>0):
            digit = num%10
            if(newnum%digit ==0):
                count+=1
            num = num//10
        return count

