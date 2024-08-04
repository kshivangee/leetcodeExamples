class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabets={}
        for i in range(97, 123):
            alphabets[chr(i)] = None
        for char in sentence:
            alphabets[char] = 1
        if(len(set(alphabets.values()))==1):
            return True
        else:
            return False