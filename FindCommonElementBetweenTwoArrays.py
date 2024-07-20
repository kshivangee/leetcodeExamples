class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numbers1 = set(nums1)
        numbers2 = set(nums2)
        common = list(numbers1&numbers2)
        nums1count, nums2count = 0,0
        for i in common:
            nums1count += nums1.count(i)
            nums2count += nums2.count(i)
        return [nums1count, nums2count]
