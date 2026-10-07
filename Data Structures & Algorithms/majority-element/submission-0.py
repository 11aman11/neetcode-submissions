class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapN = {}
        for num in nums:
            mapN[num] = 1 + mapN.get(num, 0)

            if mapN[num] > (len(nums) /2):
                return num
        
        