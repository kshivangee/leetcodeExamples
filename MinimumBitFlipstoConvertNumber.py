class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        count=0
        startbin = bin(start)[:1:-1]
        goalbin = bin(goal)[:1:-1]
        if(len(startbin)>len(goalbin)):
            goalbin += '0'*(len(startbin)-len(goalbin))
        elif(len(startbin)<len(goalbin)):
            startbin += '0'*(len(goalbin)-len(startbin))
        for i in range(len(startbin)-1,-1,-1):
            if(startbin[i]!=goalbin[i]):
                count+=1
        return count