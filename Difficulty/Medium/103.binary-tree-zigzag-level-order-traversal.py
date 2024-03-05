#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (58.64%)
# Likes:    10545
# Dislikes: 282
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = [root]
        signal = True
        temp = []
        levels = [[root.val]]

        while queue:
            s = queue.pop(0)
            if s.left : temp.append(s.left)
            if s.right : temp.append(s.right)

            if not queue:
                if temp:
                    signal = not signal
                    if signal:
                        levels.append([t.val for t in temp])
                    else:
                        levels.append([t.val for t in reversed(temp)])
                queue = temp
                temp = []
        return levels
                    



        
# @lc code=end

