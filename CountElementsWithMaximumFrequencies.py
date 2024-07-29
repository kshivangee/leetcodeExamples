class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequencies = {}
        result=0
        for i in nums:
            frequencies[i] = nums.count(i)
        frequencies = dict(sorted(frequencies.items(), key = lambda kv:kv[1], reverse=True))
        maxvalue = max(frequencies.values())
        for i,j in frequencies.items():
            if(j == maxvalue):
                result+=j
        return result



        