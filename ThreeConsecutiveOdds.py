class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)-2):
            j,k=i+1, i+2
            if(arr[i]%2!=0 and arr[j]%2!=0 and arr[k]%2!=0):
                return True
        else:
            return False
