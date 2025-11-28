class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left,right=0,len(height)-1
        while left<=right:
            smaller = min(height[left],height[right])
            curr_water = smaller*(right-left)
            max_water = max(max_water,curr_water)
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
            
        return max_water