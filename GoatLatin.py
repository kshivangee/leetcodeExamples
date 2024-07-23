class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        print words
        for i in range(len(words)):
            if(words[i][0].lower() in ['a','e','i','o','u']):
                words[i] = str(words[i][:])+'ma'+'a'* (i+1)
            else:
                words[i].replace(words[i][0],'')
                words[i] = str(words[i][1:])+str(words[i][0])+'ma'+'a'*(i+1)
        return ' '.join(words)
            



                

        