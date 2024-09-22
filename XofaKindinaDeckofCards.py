import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if(len(deck)<2):
            return False
        numbers={}
        for i in deck:
            numbers[i] = deck.count(i)
        listvalues = list(numbers.values())
        n= listvalues[0]
        for i in range(1, len(listvalues)):
            n = math.gcd(n,listvalues[i])
        return n!=1