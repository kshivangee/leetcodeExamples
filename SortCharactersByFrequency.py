class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequencies = {}
        result = ""
        for i in s:
            if(i not in frequencies):
                frequencies[i] = 1
            else:
                frequencies[i] += 1
        frequencies = sorted(frequencies.items(), key=lambda x:x[1], reverse = True)
        for k,v in frequencies:
            result+=(k*v)
        return result
