class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        result = []
        for key, value in nums.items():
            if value >= k:
                result.append(key)
        return result