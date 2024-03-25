#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (73.67%)
# Likes:    9600
# Dislikes: 348
# Total Accepted:    615.1K
# Total Submissions: 833.6K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an integer array nums of length n where all the integers of nums are in
# the range [1, n] and each integer appears once or twice, return an array of
# all the integers that appears twice.
# 
# You must write an algorithm that runs in O(n) time and uses only constant
# extra space.
# 
# 
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
# Input: nums = [1]
# Output: []
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = defaultdict(int)
        for num in nums:
            dups[num] += 1
        return [key for key, value in dups.items() if value == 2]
# @lc code=end

