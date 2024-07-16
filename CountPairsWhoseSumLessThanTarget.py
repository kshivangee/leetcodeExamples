class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            j=i+1
            while(j<len(nums)):
                if(nums[i]+nums[j]<target):
                    count+=1
                j+=1
        return count
