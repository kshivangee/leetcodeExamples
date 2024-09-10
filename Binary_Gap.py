class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_num = bin(n).replace('b','')
        print binary_num[1:]
        indexes = []
        for i in range(len(binary_num[1:])):
            if(binary_num[1:][i]=='1'):
                indexes.append(i)
        if(len(indexes)==1 and indexes[0]==0):
            return 0
        maxdiff = -1
        for i in range(1,len(indexes)):
            if(indexes[i]-indexes[i-1]>maxdiff):
                maxdiff = indexes[i]-indexes[i-1]
        return maxdiff


