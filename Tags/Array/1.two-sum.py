#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        i, j = 0, n-1
        while(i<j):
            ans = nums[i][1] + nums[j][1]
            if ans == target:
                return [nums[i][0], nums[j][0]]
            elif ans < target:
                i += 1
            else:
                j -= 1
        
# @lc code=end

