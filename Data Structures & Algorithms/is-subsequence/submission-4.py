class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
        return len(s) == i