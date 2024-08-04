class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mappings = {}
        newkey = (''.join(key.split()))
        index=0
        for i in range(len(newkey)):
            if(newkey[i] not in mappings):            
                mappings[newkey[i]] = chr(97+index)
                index+=1
            else:
                continue
        decodedmessage = ''
        for word in message:
            for char in word:
                if(char == str(' ')):
                    decodedmessage+=' '
                if(mappings.get(char)):
                    decodedmessage += mappings.get(char)
        return decodedmessage