import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hashmap = new HashMap<>();
        
        for (String c : completion) {
            if (hashmap.containsKey(c)) {
                int cnt = hashmap.get(c);
                hashmap.put(c, cnt+1);
            } else {
                hashmap.put(c, 1);
            }
        }
        
        // System.out.println(hashmap);
        
        for (String p : participant) {
            if (!hashmap.containsKey(p)) {
                answer = p;
                break;
            }
            int cnt = hashmap.get(p);
            if (cnt == 0) {
                answer = p;
                break;
            }
            hashmap.put(p, cnt-1);
        }
        
        return answer;
    }
}