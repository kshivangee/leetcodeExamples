class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        number = 0.05*len(arr)
        newarr = arr[int(number):int(len(arr)-number)]
        return float(sum(newarr))/float(len(newarr))
