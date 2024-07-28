class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        dest = {}
        for i in range(len(paths)):
            dest[paths[i][0]] = paths[i][1]
        for d in dest.values():
            if d not in dest.keys():
                return d 

        