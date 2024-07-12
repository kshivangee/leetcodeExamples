class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxwords = 0
        for i in sentences:
            countwords = len(i.split())
            if(countwords>maxwords):
                maxwords = countwords
        return maxwords

