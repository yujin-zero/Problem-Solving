import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int n : nums) {
            if (hm.containsKey(n)) {
                int tmp = hm.get(n);
                hm.put(n, tmp+1);
            } else {
                hm.put(n, 1);
            }
        }
        // System.out.println(hm);
        // System.out.println(hm.size());
        int n = nums.length;
        
        if (hm.size() >= n/2) {
            answer = n/2;
        } else {
            answer = hm.size();
        }
        
        return answer;
    }
}