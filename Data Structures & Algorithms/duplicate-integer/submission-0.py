class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for item in nums:
        #     nbTimes = nums.count(item)
        #     if nbTimes > 1:
        #         return True
        # return False
        # seen = {}
        # for item in nums:
        #     if item in seen.keys():
        #         return True
        #     else:
        #         seen[item] = False
        # return False       
        compare = set(nums)
        return True if len(compare) < len(nums) else False