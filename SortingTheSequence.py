class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words  = s.split()
        result=[0]*len(words)
        for i in words:
            index = (int(i[-1]))-1
            result[index] = i[:-1]
        return ' '.join(result)
            
            
        