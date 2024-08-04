class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target.sort()
        arr.sort()
        for i in range(len(arr)):
            if(arr[i] == target[i]):
                continue
            else:
                return False
        return True