class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for str in words:
            if(str==str[::-1]):
                return str
        return ""