#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
#
# algorithms
# Medium (62.91%)
# Likes:    2750
# Dislikes: 80
# Total Accepted:    147.8K
# Total Submissions: 235K
# Testcase Example:  '[2,2,3,3,2,4,4,4,4,4]'
#
# You are given a 0-indexed integer array tasks, where tasks[i] represents the
# difficulty level of a task. In each round, you can complete either 2 or 3
# tasks of the same difficulty level.
# 
# Return the minimum rounds required to complete all the tasks, or -1 if it is
# not possible to complete all the tasks.
# 
# 
# Example 1:
# 
# 
# Input: tasks = [2,2,3,3,2,4,4,4,4,4]
# Output: 4
# Explanation: To complete all the tasks, a possible plan is:
# - In the first round, you complete 3 tasks of difficulty level 2. 
# - In the second round, you complete 2 tasks of difficulty level 3. 
# - In the third round, you complete 3 tasks of difficulty level 4. 
# - In the fourth round, you complete 2 tasks of difficulty level 4.  
# It can be shown that all the tasks cannot be completed in fewer than 4
# rounds, so the answer is 4.
# 
# 
# Example 2:
# 
# 
# Input: tasks = [2,3,3]
# Output: -1
# Explanation: There is only 1 task of difficulty level 2, but in each round,
# you can only complete either 2 or 3 tasks of the same difficulty level.
# Hence, you cannot complete all the tasks, and the answer is -1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tasks.length <= 10^5
# 1 <= tasks[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = {}
        for task in tasks:
            if task in count.keys():
                count[task] += 1
            else:
                count[task] = 1
        if 1 in count.values(): return -1
        rounds = 0
        for num in count.values():
            rounds += ((num+2)//3)
        return rounds
        
# @lc code=end

