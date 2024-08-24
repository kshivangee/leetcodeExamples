class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumonedigit, sumtwodigit = 0,0
        for i in nums:
            if(i<10):
                sumonedigit+=i
            else:
                sumtwodigit+=i
        if(sumonedigit > sumtwodigit or sumonedigit < sumtwodigit):
            return True
        elif(sumonedigit == sumtwodigit):
            return False
        else:
            return False
