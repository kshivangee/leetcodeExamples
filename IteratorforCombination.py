from itertools import combinations
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.characters = characters
        self.combinationLength = combinationLength
        self.compute = list(combinations(self.characters, self.combinationLength))
        self.result = [''.join(i) for i in self.compute]
        self.index = 0
        
    def next(self):
        """
        :rtype: str
        """
        try:
            self.index+=1
            return self.result[self.index-1]
        except:
            pass

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            if(self.index<len(self.result)):
                return True
            else:
                return False
        except:
            pass


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()