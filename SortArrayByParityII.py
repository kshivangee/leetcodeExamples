class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd = []
        even= []
        result=[]
        for i in nums:
            if(i%2==0):
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(nums)//2):
            result.append(even[i])
            result.append(odd[i])
        return result
