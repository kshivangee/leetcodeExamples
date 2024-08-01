class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        i,j = 0,1
        count=0
        while(i<=j):   
            for j in range(i+1, len(hours)):         
                if((hours[i]+hours[j])%24==0):
                    count+=1
            i+=1
        return count