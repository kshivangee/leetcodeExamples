class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        result = []
        newscores = sorted(score,reverse=True)
        dictscores = {}
        index = 1
        for i in newscores:
            dictscores[i] = index
            index+=1
    
        for i in score:
            print i, dictscores[i]
            if(dictscores[i] == 1):
                result.append("Gold Medal")
            elif(dictscores[i] == 2):
                result.append("Silver Medal")
            elif(dictscores[i] == 3):
                result.append("Bronze Medal")
            else:
                result.append(str(dictscores[i]))
        return result
            
