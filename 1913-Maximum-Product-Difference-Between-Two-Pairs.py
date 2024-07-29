class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        small = float(inf)
        smallest = float(inf)
        big = float(-inf)
        biggest = float(-inf)
        for i in nums:
            if i > biggest:
                big = biggest
                biggest = i
                
            else:
                big = max(big, i)
            
            if i < smallest:
                small = smallest
                smallest = i
            else:
                small = min(small, i)
        
        return ((biggest * big) - (small * smallest))