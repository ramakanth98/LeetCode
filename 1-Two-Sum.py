class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ind_dict = {}

        # if len(nums)==2:
        #     if nums[0] + nums[1] == target:
        #         return [0,1]

        i = 0
        while i<len(nums):
            if target - nums[i] in ind_dict.keys():
                return [i, ind_dict[target - nums[i]]]
            else:
                ind_dict[nums[i]] = i
            i+=1
