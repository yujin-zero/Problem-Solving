import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        StringBuilder answer = new StringBuilder();
        
        String[] num_str = new String[numbers.length];
        for (int i=0; i<numbers.length; i++) {
            num_str[i] = Integer.toString(numbers[i]);
        }
        Arrays.sort(num_str, (o1, o2) -> (o2+o1).compareTo(o1+o2));
        
        for (String ns : num_str) {
            answer.append(ns);
        }
        
        if (answer.charAt(0) == '0') {
            return "0";
        }
        
        return answer.toString();
    }
}