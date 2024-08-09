class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # counts=[]
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(i+1, len(nums)):
        #         if(nums[j]<nums[i]):
        #             count+=1
        #     counts.append(count)
        # return counts

        arr= sorted(nums)
        ans = []
        for num in nums:
            com = bisect_left(arr, num)
            ans.append(com)
            del arr[com]
        return ans