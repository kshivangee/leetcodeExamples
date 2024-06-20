class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        maxCandy = max(candies)
        for i in candies:
            total = i+extraCandies
            if(total >= maxCandy):
                result.append(1)
            else:
                result.append(0)
        return result