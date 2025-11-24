/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
*/



class ValidParentheses {
    public boolean isValid(String s) {
        List<Character> input = new ArrayList<Character>();
        char[] chars= s.toCharArray();
        if(chars.length == 1)
            return false;
        for(char c:chars){
            if(c == '(' || c == '[' || c == '{')
                input.add(c);
            else if (c==')' && (input.size()!=0 && input.get(input.size() - 1)== '(')  || 
                     c==']' && (input.size()!=0 && input.get(input.size() - 1)== '[')  ||
                     c=='}' && (input.size()!=0 && input.get(input.size() - 1)== '{'))
                input.remove(input.size() - 1);
            else
                return false;
        }
        if (input.size() != 0)
            return false;

        return true;
    }
}
