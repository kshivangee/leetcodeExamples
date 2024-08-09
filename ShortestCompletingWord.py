import collections
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        license_dict = {}
        for i in licensePlate.lower():
            if(i.isalpha()):
                license_dict[i.lower()] = licensePlate.lower().count(i)
        answer = []
        for word in words:
            count = Counter(word)
            if all(count[a]>=c for a,c in license_dict.items()):
                answer.append(word)
        result = answer[0]   
        for i in answer:
            if(len(i)<len(result)):
                result = i
        return result