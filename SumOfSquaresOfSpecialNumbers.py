class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            if(len(nums) % (i+1) == 0):
                result+= nums[i]*nums[i]
        return result