class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        distinct = []
        for i in arr:
            if(arr.count(i)==1):
                distinct.append(i)
        if(len(distinct)>=k):
            return distinct[k-1]
        else:
            return ""