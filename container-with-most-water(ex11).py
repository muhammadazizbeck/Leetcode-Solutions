class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        max_water = 0
        while left < right:
            min_height = min(height[left],height[right])
            width = right-left
            max_water = max(max_water,min_height*width)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return max_water