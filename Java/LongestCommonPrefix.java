/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
*/


class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        String shortest_str="";
        int shortest_length=201;
        for(String s:strs){
            if(s.length() < shortest_length){
                shortest_str=s;
                shortest_length=s.length();
            }
        }
        // System.out.println(shortest_str);
        String common_str="";
        for(int left=0;left<shortest_length;left++){
            for(int right=left;right<shortest_length;right++){
                String subStr=shortest_str.substring(left,right);
                boolean is_common=true;
                for(String s:strs){
                    if(!s.contains(subStr))
                    is_common=false;
                }
                if(is_common && subStr.length() > common_str.length())
                common_str=subStr;
            }
        }
        return common_str;
    }
}
