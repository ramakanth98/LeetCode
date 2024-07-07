class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        unq_dict = collections.defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for i in s:
                temp[ord(i) - ord('a')] = 1 + temp[ord(i) - ord('a')]
            # j = ''.join(temp)
            unq_dict[tuple(temp)].append(s)
        return unq_dict.values()

