class Solution(object):
    def diff(self, nums1,nums2):
        result=[]
        i=0
        while(i<len(nums1)):
            if(nums1[i] not in nums2 and nums1[i] not in result):
                result.append(nums1[i])
            i+=1
        return result
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        diff1 = self.diff(nums1,nums2)
        print diff1
        diff2 = self.diff(nums2,nums1)
        print diff2
        return [diff1]+[diff2]
