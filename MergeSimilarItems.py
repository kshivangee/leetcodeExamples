class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        compute  = {}
        for i,j in items1:
            compute[i] = j
        for k,l in items2:
            if(compute.get(k)!=None):
                compute[k] += l
            else:
                compute[k] = l
        for x,y in compute.items():
            result.append([x,y])
        return sorted(result)

