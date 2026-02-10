import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();
        
        List<Character> charList = new ArrayList<>();
        for (int i=0; i<26; i++) {
            char c = (char)((int)'a' + i);
            charList.add(c);
        }
        
        for (char c : skip.toCharArray()) {
            charList.remove(Character.valueOf(c));
        }
        
        for (char c : s.toCharArray()) {
            int idx = charList.indexOf(c);
            idx += index;
            if (idx >= charList.size()) {
                idx %= charList.size();
            }
            answer.append(charList.get(idx));
        }
        
        return answer.toString();
    }
}