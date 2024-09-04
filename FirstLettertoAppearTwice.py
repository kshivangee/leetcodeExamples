class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen=set()
        for i in s:
            if(i not in seen):
                seen.add(i)
            else:
                return i