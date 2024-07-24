class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        newmappings=[]
        for number in nums:
            num= str(number)
            len_number = len(num)
            result=''
            for j in range(len_number):
                result+=str(mapping[int(num[j])])
            newmappings.append([number,int(result)])
        newmappings.sort(key=lambda kv:kv[1])
        result=[]
        for i,j in newmappings:
            result.append(i)
        return result
   

