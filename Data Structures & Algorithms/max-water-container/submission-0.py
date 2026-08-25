class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1 , len(heights)):
        #         height = min(heights[i] , heights[j])
        #         width = j - i
        #         area = width * height
        #         maxArea = max(maxArea, area)
        # return maxArea
        i, j = 0, len(heights) - 1
        while i < j:
            height = min(heights[i] , heights[j])
            width = j - i
            area = width * height
            maxArea = max(maxArea, area)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return maxArea  
            

        