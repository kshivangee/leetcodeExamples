class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        countbar, countstar = 0,0
        for i in s:
            if(i=='|'):
                countbar+=1
            if(countbar%2==0):
                if(i == '*'):
                    countstar+=1
        return countstar
            