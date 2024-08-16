class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(k):
            result += nums[-1]
            removedelement = nums[-1]
            nums.remove(nums[-1])
            nums.append(removedelement+1)
        return result