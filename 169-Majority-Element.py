class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_dict = {}

        for i in nums:
            freq_dict[i] = 1 + freq_dict.get(i, 0)
        max_val = max(freq_dict.values())
        value = [i for i in freq_dict if freq_dict[i]==max_val]
        return value[0]

        #Boyre Moore Solution with O(1) time and space complexity
        # res, count = 0, 0

        # for n in nums:
        #     if count == 0:
        #         res = n
        #     count += (1 if n == res else -1)
            
        # return res
        