class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        flag=0
        for i in words:
            word = i
            for j in word:
                if(j in allowed):
                    flag=1
                else:
                    flag=0
                    break
            if(flag==1):
                count+=1
        return count

