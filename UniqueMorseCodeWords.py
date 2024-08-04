class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dict = {}
        index=0
        for i in range(97,123):
            morse_dict[chr(i)] = morse_list[index]
            index+=1
        result = []
        for word in words:
            each = ''
            for char in word:
                each+= morse_dict[char]
            result.append(each)
        return len(set(result))
