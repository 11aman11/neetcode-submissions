class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        result = []
        sortedKeys = sorted(nums.keys())
        
        return sortedKeys[k - 1:]