class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]

        for i in range(numRows-1):
            temp_list = res[i].copy()
            temp_list.insert(0, 0)
            temp_list.append(0)
            new_list = [temp_list[i] + temp_list[i+1] for i in range(len(temp_list)-1)]
            res.append(new_list)
        return res
