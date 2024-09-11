class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        bits= date.split('-')
        result = []
        for i in bits:
            x = bin(int(i)).replace('b','')
            result.append(x[1:])
        return '-'.join(result)
