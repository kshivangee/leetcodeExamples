class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums:
            compute = []
            while(i>0):
                units = i%10
                compute.append(units)
                i = i//10
            for j in compute[::-1]:
                result.append(j)
        return result