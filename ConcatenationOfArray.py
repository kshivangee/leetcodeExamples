class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        result=[]
        while(count<2):
            for i in nums:
                result.append(i)
            count+=1
        return result
        
        #return nums+nums