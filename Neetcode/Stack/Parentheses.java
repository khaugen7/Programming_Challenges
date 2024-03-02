/**
 * Leetcode Q20 - Valid Parentheses
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 *
 * An input string is valid if:
 *
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Every close bracket has a corresponding open bracket of the same type.
 *
 *
 * Example 1:
 *
 * Input: s = "()"
 * Output: true
 * Example 2:
 *
 * Input: s = "()[]{}"
 * Output: true
 * Example 3:
 *
 * Input: s = "(]"
 * Output: false
 *
 *
 * Constraints:
 *
 * 1 <= s.length <= 104
 * s consists of parentheses only '()[]{}'.
 */

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        char c;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            }
            else {
                if (stack.isEmpty())
                    return false;
                switch(c) {
                    case ')':
                        if (stack.pop() != '(')
                            return false;
                        else
                            break;
                    case ']':
                        if (stack.pop() != '[')
                            return false;
                        else
                            break;
                    case '}':
                        if (stack.pop() != '{')
                            return false;
                        else
                            break;
                }
            }
        }
        return stack.isEmpty();
    }
}