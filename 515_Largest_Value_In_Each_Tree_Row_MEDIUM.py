# 515. Find Largest Value in Each Tree Row - Medium

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Example 2:
# Input: root = [1,2,3]
# Output: [1,3]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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