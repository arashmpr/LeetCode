/*
 * @lc app=leetcode id=345 lang=cpp
 *
 * [345] Reverse Vowels of a String
 *
 * https://leetcode.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (52.73%)
 * Likes:    4394
 * Dislikes: 2760
 * Total Accepted:    793.5K
 * Total Submissions: 1.5M
 * Testcase Example:  '"hello"'
 *
 * Given a string s, reverse only all the vowels in the string and return it.
 * 
 * The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
 * lower and upper cases, more than once.
 * 
 * 
 * Example 1:
 * Input: s = "hello"
 * Output: "holle"
 * Example 2:
 * Input: s = "leetcode"
 * Output: "leotcede"
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 3 * 10^5
 * s consist of printable ASCII characters.
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    string reverseVowels(string s) {
        int i = 0;
        int j = s.size() - 1;
        set<char> v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        while (i<j) {
            while(i<j && (v.find(s[i]) == v.end())) {
                i++;
            }
            while(i<j && (v.find(s[j]) == v.end())) {
                j--;
            }
            char t = s[i];
            s[i] = s[j];
            s[j] = t;
            i++;
            j--;
        }
        return s;
    }
};
// @lc code=end

