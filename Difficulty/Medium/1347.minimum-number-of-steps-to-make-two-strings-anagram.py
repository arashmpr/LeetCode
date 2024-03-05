#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
#
# algorithms
# Medium (81.98%)
# Likes:    2669
# Dislikes: 117
# Total Accepted:    266.5K
# Total Submissions: 325K
# Testcase Example:  '"bab"\n"aba"'
#
# You are given two strings of the same length s and t. In one step you can
# choose any character of t and replace it with another character.
# 
# Return the minimum number of steps to make t an anagram of s.
# 
# An Anagram of a string is a string that contains the same characters with a
# different (or the same) ordering.
# 
# 
# Example 1:
# 
# 
# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of
# s.
# 
# 
# Example 2:
# 
# 
# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters
# to make t anagram of s.
# 
# 
# Example 3:
# 
# 
# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams. 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# s.length == t.length
# s and t consist of lowercase English letters only.
# 
# 
#

# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_words = {}
        for x in s:
            if x in s_words.keys():
                s_words[x] += 1
            else:
                s_words[x] = 1
        
        step = 0
        for x in t:
            if x in s_words.keys():
                if s_words[x]:
                    s_words[x] -= 1
                else:
                    step += 1
            else:
                step += 1
        
        return step
        
# @lc code=end

