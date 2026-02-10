import java.util.*;

class Solution {
    public int[] solution(String s) {
        int lenS = s.length();
        int[] answer = new int[lenS];
        
        HashMap<Character, Integer> alpha = new HashMap<>();
        
        for (int i=0; i<lenS; i++) {
            char currentChar = s.charAt(i);
            
            if (alpha.containsKey(currentChar)) {
                answer[i] = i - alpha.get(currentChar);
                alpha.put(currentChar, i);
            } else {
                answer[i] = -1;
                alpha.put(currentChar, i);
            }
        }
        
        
        
        return answer;
    }
}