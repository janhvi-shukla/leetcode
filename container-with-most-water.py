class Solution:
    def maxArea(self,height):
        maxArea=0
        n=len(height)
        for i in range(n):
            for j in range(i+1,n):
                area=min(height[i],height[j])*(j-i)
                maxArea=max(maxArea,area)
        return maxArea

    
