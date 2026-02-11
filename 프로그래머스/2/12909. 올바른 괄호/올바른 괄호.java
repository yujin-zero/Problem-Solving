import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push('(');
            } else {
                if (stack.size() == 0) {
                    answer = false;
                    break;
                } else {
                    if (stack.peek() == '(') {
                        stack.pop();
                    } else {
                        answer = false;
                        break;
                    }
                }
            }
        }
        
        if (stack.size() > 0) {
            answer = false;
        }
        
        return answer;
    }
}