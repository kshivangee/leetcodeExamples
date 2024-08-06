class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        compute = []
        M = 1000000007
        for i in range(len(nums)):
            value = 0
            for j in range(i,len(nums)):
                value += nums[j]
                compute.append(value)
        # print compute
        compute.sort()
        return (sum(compute[left-1:right]))%M
