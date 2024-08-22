class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = (bin(num)).replace('b','')
        listbin = list(binary)
        del listbin[0]
        for i in range(len(listbin)):
            if(listbin[i]=='1'):
                listbin[i] = '0'
            elif(listbin[i]=='0'):
                listbin[i] = '1'
            else:
                continue
        compute = ''.join(listbin)
        result = int(compute,2)
        return result
