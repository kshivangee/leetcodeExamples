class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if(len(nums)==1):
            return float(nums[0])
        currsum = sum(nums[:k])
        summax = sum(nums[:k])
        for i in range(k,len(nums)):
            currsum += nums[i] -nums[i-k]  
            summax = max(currsum, summax)
         
        return float(summax)/float(k)
