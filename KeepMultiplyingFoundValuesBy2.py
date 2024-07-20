class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        for ele in nums:
            if(original in nums):
                original= original*2
            else:
                return original
        return original
