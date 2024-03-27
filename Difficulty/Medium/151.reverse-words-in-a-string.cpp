/*
 * @lc app=leetcode id=151 lang=cpp
 *
 * [151] Reverse Words in a String
 *
 * https://leetcode.com/problems/reverse-words-in-a-string/description/
 *
 * algorithms
 * Medium (41.25%)
 * Likes:    8089
 * Dislikes: 5083
 * Total Accepted:    1.4M
 * Total Submissions: 3.4M
 * Testcase Example:  '"the sky is blue"'
 *
 * Given an input string s, reverse the order of the words.
 * 
 * A word is defined as a sequence of non-space characters. The words in s will
 * be separated by at least one space.
 * 
 * Return a string of the words in reverse order concatenated by a single
 * space.
 * 
 * Note that s may contain leading or trailing spaces or multiple spaces
 * between two words. The returned string should only have a single space
 * separating the words. Do not include any extra spaces.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "the sky is blue"
 * Output: "blue is sky the"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "  hello world  "
 * Output: "world hello"
 * Explanation: Your reversed string should not contain leading or trailing
 * spaces.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "a good   example"
 * Output: "example good a"
 * Explanation: You need to reduce multiple spaces between two words to a
 * single space in the reversed string.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s contains English letters (upper-case and lower-case), digits, and spaces '
 * '.
 * There is at least one word in s.
 * 
 * 
 * 
 * Follow-up: If the string data type is mutable in your language, can you
 * solve it in-place with O(1) extra space?
 * 
 */

// @lc code=start
class Solution {
public:
    string reverseWords(string s) {
        vector<string> ws;
        stringstream ss(s);
        string w;

        while(getline(ss, w, ' ')) {
            if (!w.empty()) {
                ws.push_back(w);
            }
        }

        int i = 0;
        int j = (ws.size()-1);

        while(i<j) {
            string temp = ws[i];
            ws[i] = ws[j]; 
            ws[j] = temp;

            i++;
            j--;
        }
        string res = "";
        for (i=0 ; i < ws.size()-1 ; i++) {
            res += (ws[i] + " ");
        }

        return (res + ws[i]);
    }
};
// @lc code=end

