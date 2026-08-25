class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = defaultdict(int)
        for item in arr:
            freq[item] += 1
        count = 0
        for key in freq:
            if freq[key] == 1:
                count += 1
            
            if count == k:
                return key
        return ""

