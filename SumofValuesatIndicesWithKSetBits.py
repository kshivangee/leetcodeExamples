class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result=0
        for num in range(len(nums)):
            if(bin(num).replace('b','').count('1')==k):
                result+=nums[num]
        return result
        