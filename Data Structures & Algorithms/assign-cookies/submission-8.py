class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i , j = 0, 0 
        s.sort()
        g.sort()
        
        while i < len(g):
            while j < len(s) and g[i] > s[i]:
                j += 1
            if j == len(s):
                break
            j += 1
            i += 1
        return i