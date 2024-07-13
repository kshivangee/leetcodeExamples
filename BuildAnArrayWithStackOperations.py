class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result=[]
        stack=[]
        for i in range(1,n+1):
            if(stack==target):
                break
            elif(i in target):
                stack.append(i)
                result.append("Push")
            elif(i not in target):
                stack.append(i)
                stack.remove(stack[-1])
                result.extend(["Push","Pop"])
        return result


            

        