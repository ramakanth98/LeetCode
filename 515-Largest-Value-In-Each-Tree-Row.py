
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        st = [(root, 0)]
        if not root:
            return
        res = [root.val]
        max1 = {0:root.val}
        while st:
            x, lev = st.pop()
            max1[lev] = max(max1.get(lev, -inf), x.val)
            if x.left:
                st.append((x.left, lev+1))
            if x.right:
                st.append((x.right, lev+1))
        return max1.values()      