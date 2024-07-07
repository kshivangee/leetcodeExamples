class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for i in operations:
            if(i == '--X'):
                x-=1
            if(i == 'X++'):
                x+=1
            if(i == 'X--'):
                x-=1
            if(i == '++X'):
                x+=1
        return x
