class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        for r in range(len(t)):
            if s[l] == t[r]:
                l += 1
        return l == len(s)
        