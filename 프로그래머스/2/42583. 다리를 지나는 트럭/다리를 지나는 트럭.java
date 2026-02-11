import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int sec = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i=0; i<bridge_length; i++) {
            queue.offer(0);
        }
        // System.out.println(queue);
        
        int idx = 0;
        int currentWeight = 0;
        while (true) {
            int outTruck = queue.poll();
            currentWeight -= outTruck;
            
            if (idx < truck_weights.length) {
                int nextTruck = truck_weights[idx];
                if (nextTruck + currentWeight <= weight) {
                    queue.offer(nextTruck);
                    currentWeight += nextTruck;
                    idx++;
                } else {
                    queue.offer(0);
                }
            } else {
                queue.offer(0);
            }
            
            sec++;
            
            if (currentWeight == 0) {
                answer = sec;
                break;
            }
        }
        
        
        return answer;
    }
}