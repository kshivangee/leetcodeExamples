class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums)==1):
            return nums
        nums1=sorted(nums[:len(nums)//2])
        nums2=sorted(nums[len(nums)//2:])
        print nums1, nums2
        i,j=0,0
        result=[]
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<nums2[j]):
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        while(i<len(nums1)):
            result.append(nums1[i])
            i+=1
        while(j<len(nums2)):
            result.append(nums2[j])
            j+=1
        return result


        