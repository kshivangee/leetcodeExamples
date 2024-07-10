class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_list = []
        result=""
        for char in s:
            if(char in ['a','e','i','o','u','A','E','I','O','U']):
                vowels_list.append(char)
        vowels_list.sort()
        index=0
        for i in range(len(s)):
            if(s[i] in ['a','e','i','o','u','A','E','I','O','U']):
                result += vowels_list[index]
                index+=1
            else:
                result+=s[i]
        return result






        