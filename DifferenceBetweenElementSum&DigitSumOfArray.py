class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumnums= sum(nums)
        digitsum=0
        for i in nums:
            if(i>=10):
                while(i>0):
                    digitsum += i%10
                    i=i//10
            else:
                digitsum+=i
        return abs(sumnums-digitsum)
