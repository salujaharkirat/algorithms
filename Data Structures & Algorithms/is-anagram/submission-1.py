from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for pos in range(len(s)):
            countS[s[pos]] = 1 + countS.get(s[pos], 0)
            countT[t[pos]] = 1 + countT.get(t[pos], 0)
        
        return countS == countT


        