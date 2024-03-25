/*
 * @lc app=leetcode id=605 lang=cpp
 *
 * [605] Can Place Flowers
 *
 * https://leetcode.com/problems/can-place-flowers/description/
 *
 * algorithms
 * Easy (29.32%)
 * Likes:    6333
 * Dislikes: 1128
 * Total Accepted:    721.1K
 * Total Submissions: 2.5M
 * Testcase Example:  '[1,0,0,0,1]\n1'
 *
 * You have a long flowerbed in which some of the plots are planted, and some
 * are not. However, flowers cannot be planted in adjacent plots.
 * 
 * Given an integer array flowerbed containing 0's and 1's, where 0 means empty
 * and 1 means not empty, and an integer n, return true if n new flowers can be
 * planted in the flowerbed without violating the no-adjacent-flowers rule and
 * false otherwise.
 * 
 * 
 * Example 1:
 * Input: flowerbed = [1,0,0,0,1], n = 1
 * Output: true
 * Example 2:
 * Input: flowerbed = [1,0,0,0,1], n = 2
 * Output: false
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= flowerbed.length <= 2 * 10^4
 * flowerbed[i] is 0 or 1.
 * There are no two adjacent flowers in flowerbed.
 * 0 <= n <= flowerbed.length
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int l = flowerbed.size();
        if (n==0) {
            return true;
        }
        if (l == 1) {
            if (flowerbed[0]==0) {
                return n<=1 ? true : false;
            } else {
                return n==0 ? true : false;
            }
        }
        for(int i=0 ; i<l; i++) {
            if (flowerbed[i] == 0) {
                if (i==0 || i==l-1) {
                    if (i==0) { 
                        if (flowerbed[i+1] == 0) {
                            flowerbed[i] = 1;
                            n--;
                        }
                    } 
                    else {
                        if (flowerbed[i-1] == 0) {
                            flowerbed[i] = 1;
                            n--;
                        }
                    }
                } else {
                    if (flowerbed[i-1] == 0 && flowerbed[i+1] == 0) {
                        flowerbed[i] = 1;
                        n--;
                    }
                }
            }
            if (n == 0) {
                return true;
            }
        }
        return false;
    }
};
// @lc code=end

