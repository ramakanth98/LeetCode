class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        res = 0

        if len(arr)==1:
            if arr[0]==0:
                if n<2:
                    return True
            else:
                if n>0:
                    return False
                return True

        for i in range(len(arr)-1):
            if arr[i]==0:
                if i!=0:
                    if arr[i-1]!=1 and arr[i+1]!=1:
                        arr[i]=1
                        res+=1
                else:
                    if arr[i+1]!=1:
                        arr[i]=1
                        res+=1
            if res>=n:
                return True
        if arr[-1]==0 and arr[-2]==0:
            res+=1
        return(res==n)