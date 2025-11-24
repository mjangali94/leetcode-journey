/*
Given a string s, find the length of the longest substring without duplicate characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
*/


class LengthOfLongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        
        int maxLength=0;
        Set<Character> chars=new HashSet<Character>();
        int left= 0;
        int right=0;

        while(right < s.length()){
            char c= s.charAt(right);
            while(chars.contains(c)){
                chars.remove(s.charAt(left));
                left++;
            }
            chars.add(c);
            maxLength = Math.max(maxLength, right-left+1);
            right++;
            
        }

        return maxLength;
    }
}
