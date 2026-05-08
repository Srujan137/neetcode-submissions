class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l , r = 0 , len(heights) - 1

        while l < r:
            width = r - l
            length = min(heights[r], heights[l])
            area = width * length
            maxarea = max(area, maxarea)  
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1      


        for i in range(0,len(heights)):
            for j in range(0,len(heights)):
                width = j-i
                length = min(heights[i], heights[j])
                area = width * length
                maxarea = max(area, maxarea)
                #print(heights[i], heights[j], width, length, area, maxarea)
        
        return maxarea
        