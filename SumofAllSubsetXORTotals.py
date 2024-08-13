from itertools import combinations
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subsets = []
        result = 0
        for i in range(len(nums)+1):
            subsets.extend(combinations(nums,i))
        for i in range(1,len(subsets)):
            x = list(subsets[i])
            if(len(x)>1):
                for j in range(len(x)):
                    if(j==0):
                        compute = x[j]
                    else:
                        compute ^= x[j]
                result+=compute

            else:
                result+=x[0]
        return result