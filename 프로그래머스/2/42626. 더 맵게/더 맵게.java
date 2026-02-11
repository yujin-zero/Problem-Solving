import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : scoville) {
            pq.offer(s);
        }
        // System.out.println(pq);
        
        while (true) {
            int min_value = pq.peek(); 
            
            if (min_value >= K) {
                break;
            }
            
            // 2개 안남음
            if (pq.size() < 2) {
                answer = -1;
                break;
            }
            
            int min1 = pq.poll();
            int min2 = pq.poll();
            
            int new_scoville = min1 + min2 * 2;
            pq.offer(new_scoville);
            answer++;
        }
        
        
        return answer;
    }
}