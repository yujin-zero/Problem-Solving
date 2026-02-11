import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int n = progresses.length;
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i=0; i<n; i++) {
            int tmp = (100-progresses[i]) / speeds[i];
            if ((100-progresses[i]) % speeds[i] == 0) {
                queue.offer(tmp);
            } else {
                queue.offer(tmp+1);
            }
        }
        // System.out.println(queue);
        
        
        while (!queue.isEmpty()) {
            int value = queue.poll();
            // System.out.println(value);
            
            int cnt = 1;
            while (!queue.isEmpty() && queue.peek() <= value) {
                queue.poll();
                cnt++;
            }
            answer.add(cnt);
        }
        
        int[] result = new int[answer.size()];
        for (int i=0; i<answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}