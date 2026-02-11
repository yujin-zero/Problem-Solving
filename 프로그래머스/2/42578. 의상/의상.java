import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, Integer> hm = new HashMap<>();
        for (String[] clo : clothes) {
            String name = clo[0];
            String type = clo[1];
            
            if (hm.containsKey(type)) {
                hm.put(type, hm.get(type)+1);
            } else {
                hm.put(type, 1);
            }
        }
        
        for (String t : hm.keySet()) {
            int cnt = hm.get(t);
            answer *= (cnt+1);
        }
        answer--;
        
        return answer;
    }
}