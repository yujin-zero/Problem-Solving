import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        List<Integer> cit_list = new ArrayList<>();
        for (int c : citations) {
            cit_list.add(c);
        }
        Collections.sort(cit_list, Collections.reverseOrder());

        for (int i=0; i<citations.length; i++) {
            if (i+1 <= cit_list.get(i)) {
                answer = i+1;
            } else {
                break;
            }
        }
        
        return answer;
    }
}