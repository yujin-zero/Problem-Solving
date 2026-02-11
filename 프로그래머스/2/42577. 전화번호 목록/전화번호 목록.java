import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        List<String> pb = new ArrayList<>(Arrays.asList(phone_book));
        Collections.sort(pb);

        for (int i=0; i<phone_book.length-1; i++) {
            String current = pb.get(i);
            String next = pb.get(i+1);
            
            int current_len = current.length();
            if (next.length() < current_len) {
                continue;
            }
            
            if (current.equals(next.substring(0, current_len))) {
                answer = false;
                break;
            }
            
        }
        
        return answer;
    }
}