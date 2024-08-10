class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxval=-1
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(abs(nums[i]-nums[j])<=min(nums[i],nums[j])):
                    if(nums[i]^nums[j]>maxval):
                        maxval = nums[i]^nums[j]
        return maxval