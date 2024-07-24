class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numslist=nums
        self.presum=sum(self.numslist)

        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.presum = self.presum-self.numslist[index]+val
        self.numslist[index] = val
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.presum - sum(self.numslist[:left])-sum(self.numslist[right+1:])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)