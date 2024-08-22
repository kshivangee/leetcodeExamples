class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = sorted(nums+[target]) if target not in nums else nums
        value = 0
        for i in range(len(result)):
            if(result[i]==target):
                value = i
        return value
        
            

        
