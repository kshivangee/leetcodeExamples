class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        print(words)
        res=' '.join(words[::-1])
        return res
        