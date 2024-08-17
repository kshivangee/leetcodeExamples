class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 0
        repeatedword = word
        while(repeatedword in sequence):
            repeatedword += word
            count+=1
        return count