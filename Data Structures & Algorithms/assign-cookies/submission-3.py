class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left = 0
        right = 0
        fed = 0
        g = sorted(g)
        s = sorted(s)
        while left < len(g) and right < len(s):
            if s[right] >= g[left]:
                fed += 1
                left += 1
            
            right += 1
        return fed
