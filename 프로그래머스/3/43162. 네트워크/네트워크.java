import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visit = new boolean[n]; // false
        // for (int i=0; i<n; i++) {
        //     System.out.print(visit[i]);
        //     System.out.print(" ");
        // }
        
        Queue<Integer> queue = new LinkedList<>();
        // queue.offer(0);
        // queue.peek();
        // queue.poll();
        // System.out.println(queue.isEmpty());
        for (int i=0; i<n; i++) {
            if (visit[i]) {
                continue;
            }
            // System.out.println("------");
            // System.out.println("i:" + i);
            visit[i] = true;
            queue.offer(i);
            answer++;
            
            while (!queue.isEmpty()) {
                 int value = queue.poll();
                
                for (int j=0; j<n; j++) {
                    if (computers[value][j] == 1 && !visit[j]) {
                        visit[j] = true;
                        queue.offer(j);
                    }
                }
            }
        }
        
        return answer;
    }
}