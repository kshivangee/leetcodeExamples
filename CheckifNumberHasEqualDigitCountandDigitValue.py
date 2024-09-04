class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        flag=0
        for i in range(len(num)):
            if(int(num.count(str(i)))==int(num[i])):
                flag=1
            else:
                flag=0
                break
        if(flag==1):
            return True
        else:
            return False
