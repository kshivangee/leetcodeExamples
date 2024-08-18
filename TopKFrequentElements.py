class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequencies = {}
        result = []
        for i in nums:
            if(i not in frequencies):
                frequencies[i] = 1
            else:
                frequencies[i]  += 1
        frequencies = sorted(frequencies.items(), key = lambda x:x[1], reverse=True)
        for x,y in frequencies:
            if(len(result)!=k):
                result.append(x)
        return result
