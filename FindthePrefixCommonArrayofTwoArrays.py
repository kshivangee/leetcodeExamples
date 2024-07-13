class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        #Solution 1: Using sets
        # C=[]
        # set1, set2 = set() , set()
        # for a,b in zip(A,B):
        #     set1.add(a)
        #     set2.add(b)
        #     C.append(len(set1 & set2))
        # return C
        
        
        #Solution 2: Using dictionary
        C = []
        frequency = {}
        for index in range(len(A)):
            if(A[index] in frequency.keys()):
                frequency[A[index]] += 1
            else:
                frequency[A[index]] = 1
            if(B[index] in frequency.keys()):
                frequency[B[index]] += 1
            else:
                frequency[B[index]] = 1
            if(frequency[A[index]] == 1 and frequency[A[index]] == 1 and len(frequency)==1):
                C.append(0)
            else:
                count = [key for (key,value) in frequency.items() if value>1]
                C.append(len(count))
        return C

