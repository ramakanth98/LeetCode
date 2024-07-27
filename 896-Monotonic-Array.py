class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        
        check = nums[-1] - nums[0]
        if check <= 0:
            nums = nums[::-1]
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
