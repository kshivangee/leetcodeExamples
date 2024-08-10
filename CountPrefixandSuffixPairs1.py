class Solution(object):
    def isPrefixAndSuffix(self,word1, word2):
        if(word2.startswith(word1) and word2.endswith(word1)):
            return True
        else:
            return False
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if(i<j):
                    if(self.isPrefixAndSuffix(words[i], words[j]) == True):
                        count+=1

        return count
