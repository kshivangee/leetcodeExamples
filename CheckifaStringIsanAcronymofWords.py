class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        result = ''
        for i in words:
            result += i[0]
        return result == s