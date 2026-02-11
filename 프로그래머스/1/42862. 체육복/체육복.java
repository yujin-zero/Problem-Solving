import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i=1; i<n+1; i++) {
            hm.put(i, 1);
        }
        hm.put(0, 0);
        hm.put(n+1, 0);
        
        for (int l : lost) {
            hm.put(l, hm.get(l)-1);
        }
        for (int r : reserve) {
            hm.put(r, hm.get(r)+1);
        }
        
        for (int i=1; i<n+1; i++) {
            if (hm.get(i) > 0) {
                answer++;
            } else {
                if (hm.get(i-1) > 1) {
                    answer++;
                    hm.put(i-1, hm.get(i-1)-1);
                    hm.put(i, 1);
                } else if (hm.get(i+1) > 1) {
                    answer++;
                    hm.put(i+1, hm.get(i+1)-1);
                    hm.put(i, 1);
                }
            }
        }
        
        return answer;
    }
}