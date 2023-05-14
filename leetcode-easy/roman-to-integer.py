class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        romanDict = {"I":1, 
                     "V":5,
                     "X":10,
                     "L":50,
                     "C":100,
                     "D":500,
                     "M":1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romanDict[s[i]] < romanDict[s[i+1]]:
                res = res - romanDict[s[i]]
            else:
                res = res + romanDict[s[i]]
        return res