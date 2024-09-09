class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        for i in range(len(word)):
            if(word[i]==ch):
                reverse = word[:i+1][::-1]
                return reverse + word[i+1:]
        else:
            return word