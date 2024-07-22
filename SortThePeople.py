class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        names_heights={}
        for i in range(len(names)):
            names_heights[heights[i]] = names[i]
        print names_heights
        heights_keys = sorted(names_heights.keys(),reverse=True)
        print heights_keys
        result = [names_heights[i] for i in heights_keys]
        return result


        