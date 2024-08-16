class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        counts = {5:0, 10:0}
        for i in bills:
            if(i==5):
                counts[5]+=1
            elif(i==10):
                if(counts[5]):
                    counts[5]-=1
                    counts[10]+=1
                else:
                    return False
            else:
                if(counts[10] and counts[5]):
                    counts[5]-=1
                    counts[10]-=1
                elif(counts[5]>=3):
                    counts[5]-=3
                else:
                    return False
        return True


                