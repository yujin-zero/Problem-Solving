import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        
        Stack<Integer> stack = new Stack<>();
        for (int ing : ingredient) {
            stack.add(ing);
            int stack_size = stack.size();
            if (ing == 1 && stack_size >= 4) {
                int t1 = stack.get(stack_size-4);
                int t2 = stack.get(stack_size-3);
                int t3 = stack.get(stack_size-2);
                
                if (t1 == 1 && t2 == 2 && t3 == 3) {
                    answer++;
                    stack.pop();
                    stack.pop();
                    stack.pop();
                    stack.pop();
                }
            }
        }
        
        return answer;
    }
}