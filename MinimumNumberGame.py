class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in range(1,len(nums)):
            if(i%2!=0):
                nums[i],nums[i-1] = nums[i-1], nums[i]
        return nums