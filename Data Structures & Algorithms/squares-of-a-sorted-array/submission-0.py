class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        factor = len(nums)
        l = 0
        r = len(nums) - 1
        result = [0] * factor
        for i in range(len(nums) - 1, - 1, - 1):
            if abs(nums[l]) < abs(nums[r]):
                result[i] = nums[r]**2
                r -= 1
            else:
                result[i] = nums[l]**2
                l += 1
        return result
            
        