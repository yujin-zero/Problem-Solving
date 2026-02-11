import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        for (int p : priorities) {
            queue.offer(p);
        }
        // System.out.println(queue);
        // System.out.println(Collections.max(queue));
        
        int processCnt = 0;
        
        while (!queue.isEmpty()) {
            int value = queue.poll();
            
            // 아무것도 없을 때 처리
            if (queue.isEmpty()) {
                processCnt++;
                answer = processCnt;
                break;
            }
            
            if (value < Collections.max(queue)) {
                queue.offer(value);
                if (location == 0) {
                    location = queue.size()-1;
                } else {
                    location--;
                }
            } else {
                processCnt++;
                if (location == 0) {
                    answer = processCnt;
                    break;
                } else {
                    location--;
                }
            }
        }
        
        return answer;
    }
}