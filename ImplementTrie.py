class TrieNode:
    def __init__(self):
        self.childnode = [None]*26
        self.wordend=False

class Trie(object):
    def __init__(self):
        # self.list1=[]
        #Approach 2: Using Trie data structure
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        # self.list1.append(word)
        
        current = self.root
        for i in word:
            index = ord(i)-ord('a')
            if(not current.childnode[index]):
                current.childnode[index]= TrieNode()
            current = current.childnode[index]
        current.wordend=True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # try:
        #     if(word in self.list1):
        #         return True
        #     else:
        #         return False
        # except:
        #     pass
        
        current = self.root
        for i in word:
            index = ord(i)-ord('a')
            if(current.childnode[index] is None):
                return False
            current = current.childnode[index]
        return current.wordend
    
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        # try:
        #     for i in self.list1:
        #         if(i.startswith(prefix)):
        #             return True
        #     else:
        #         return False
        # except:
        #     pass
        
        current = self.root
        for i in prefix:
            index=ord(i)-ord('a')
            if(current.childnode[index] is None):
                return False
            current = current.childnode[index]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
