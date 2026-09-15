class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        arr = []
        for key, value in nums.items():
            arr.append([value, key])

        arr = sorted(arr)
        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        return result

        