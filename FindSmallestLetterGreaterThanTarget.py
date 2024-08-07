# import sys
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        result = ''
        mindiff = 0
        for i in letters:
            if(ord(i)>ord(target)):
                result += i
                break
        else:
            result = letters[0]
        return result