class MyQueue(object):

    def __init__(self):
        self.list1=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        try:
            element = self.list1[0]
            self.list1.remove(element)
            return element
        except:
            pass
       
    def peek(self):
        """
        :rtype: int
        """
        try:
            return self.list1[0]
        except:
            pass
       
    def empty(self):
        """
        :rtype: bool
        """
        try:
            return self.list1==[]
        except:
            pass
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()