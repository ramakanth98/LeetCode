class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        tot_sum = sum(nums)
        l_sum = 0

        for i in range(len(nums)):
            # l_sum += nums[i]
            r_sum = tot_sum - l_sum - nums[i]
            if r_sum == l_sum:
                return i
            l_sum += nums[i]
        return -1
                