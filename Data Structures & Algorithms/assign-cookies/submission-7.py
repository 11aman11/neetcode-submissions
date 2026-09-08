class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i , j = 0, 0 
        s.sort()
        g.sort()
        print(s, g)
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j += 1
            i += 1
        return j