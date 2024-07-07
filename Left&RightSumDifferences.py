class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum1, rightSum1=[], []
        leftSum, rightSum= 0,0
        for i in range(len(nums)):
            if(i==0):
                leftSum1.append(0)
            else:
                leftSum += nums[i-1]
                leftSum1.append(leftSum)
        for i in range(len(nums)-1,-1,-1):
            print i
            if(i==len(nums)-1):
                rightSum1.append(0)
            else:
                rightSum += nums[i+1]
                rightSum1.append(rightSum)
        rightSum1 = rightSum1[::-1]
        answer=[]
        for i in range(len(nums)):
            answer.append(abs(leftSum1[i]-rightSum1[i]))
        return answer


