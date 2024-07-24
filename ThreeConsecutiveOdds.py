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


     #Approach 2
        flag=0
        for i in range(0,len(arr)-2):
            print arr[i], arr[i+1], arr[i+2]
            if(arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0):
                flag=1
                break
            else:
                flag=0
        if(flag==1):
            return True
        else:
            return False
