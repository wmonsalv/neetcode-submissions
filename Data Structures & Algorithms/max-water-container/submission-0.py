class Solution:
    def maxArea(self, heights: List[int]) -> int:
        rightp = len(heights)-1
        leftp = 0 
        area = 0 
        for k in range(len(heights)):
            answer = (rightp - leftp) * min(heights[leftp], heights[rightp])
            if answer>area:
                area = answer
            if heights[leftp] == min(heights[leftp], heights[rightp]):
                leftp+= 1
            else:
                rightp-= 1
        return area 