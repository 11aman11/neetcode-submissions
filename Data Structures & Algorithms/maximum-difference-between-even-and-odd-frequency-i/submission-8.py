class Solution:
    def maxDifference(self, s: str) -> int:
        freq = defaultdict(int)
        for item in s:
            freq[item] += 1
        maxO, maxE = 1, float("+inf")
        for ch in freq:
            if freq[ch] % 2 == 0 and freq[ch] < maxE:
                maxE = freq[ch]
            if freq[ch] % 2 == 1 and freq[ch] > maxO:
                maxO = freq[ch]
        out = maxO - maxE
        return out
        
        