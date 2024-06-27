class Trie(object):

    def __init__(self):
        self.list1=[]

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.list1.append(word)
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        try:
            if(word in self.list1):
                return True
            else:
                return False
        except:
            pass
    

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        try:
            for i in self.list1:
                if(i.startswith(prefix)):
                    return True
            else:
                return False
        except:
            pass
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)