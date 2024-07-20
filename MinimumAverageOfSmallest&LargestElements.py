import sys
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        average = []
        repeat = len(nums)//2
        times=0
        while(times<repeat):
            minelement, maxelement = sys.maxint, -sys.maxint
            for number in nums:
                if(number>maxelement):
                    maxelement=number
                if(number<minelement):
                    minelement=number
            nums.remove(maxelement)
            nums.remove(minelement)
            average.append(float(maxelement+minelement)/2)
            times+=1
        return min(average)