class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequencies = {}
        for i in nums:
            frequencies[i] = nums.count(i)
        sorted_dict = sorted(frequencies.items(), key = lambda kv: (kv[1],-kv[0]))
        result=[]
        for i in sorted_dict:
            for j in range(i[1]):
                result.append(i[0])
        return result
