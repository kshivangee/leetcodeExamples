class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        rodrings = {}
        for i in range(0,len(rings),2):
            if(rodrings.get(rings[i+1]) is None):
                rodrings[rings[i+1]] = list(str(rings[i]))
            else:
                rodrings[rings[i+1]].append(str(rings[i]))
        count= 0
        for i, j in rodrings.items():
            if({'B','G','R'} == set(j)):
                count+=1
        return count

        
        