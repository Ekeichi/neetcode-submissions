class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            h_left = heights[left]
            h_right = heights[right]
            
            # Si la hauteur gauche est plus petite, c'est elle qui limite l'aire.
            if h_left < h_right:
                area = h_left * (right - left)
                if area > max_area:
                    max_area = area
                left += 1
                
            # Sinon, c'est la hauteur droite qui limite.
            else:
                area = h_right * (right - left)
                if area > max_area:
                    max_area = area
                right -= 1
        
        return max_area