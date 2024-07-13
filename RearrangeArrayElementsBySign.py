class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive_nums = [num for num in nums if num>0]
        negative_nums = [num for num in nums if num<0]
        print(positive_nums, negative_nums)
        i,j = 0,0
        result=[]
        while(i<len(positive_nums) and j<len(negative_nums)):
            result.extend([positive_nums[i],negative_nums[j]])
            i+=1
            j+=1
        return result

