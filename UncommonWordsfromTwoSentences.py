class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1words = {}
        s2words = {}
        result=[]

        for i in s1.split():
            s1words[i] = s1.count(i)
        for i in s2.split():
            s2words[i] = s2.count(i)
        for i in s1words.keys():
            if(i not in s2words.keys() and s1.split().count(i)==1):
                result.append(i)
        for i in s2words.keys():
            if(i not in s1words.keys() and s2.split().count(i)==1):
                result.append(i)
        return result