import java.util.*;

class Solution {
    int answer;
    
    public int solution(int n, int[][] wires) {
        answer = n+1;
        
        List<int[]> wires_list = new ArrayList<>();
        for (int[] wire : wires) {
            wires_list.add(wire);
        }
        
        int m = wires.length;
        for (int i=0; i<m; i++) {
            int[] tmp = wires[i];
            wires_list.remove(i);
            // System.out.println();
            // for (int[] tt : wires_list) {
            //     System.out.print(tt[0]);
            //     System.out.print(" ");
            //     System.out.print(tt[1]);
            //     System.out.print(" ");
            // }
            bfs(wires_list, n);
            wires_list.add(i, tmp);
        }
        
        return answer;
    }
    
    public void bfs(List<int[]> wires, int n) {
        boolean[] visit = new boolean[n+1];
        List<List<Integer>> graph = new ArrayList<>();
        
        for (int i=0; i<n+1; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] w : wires) {
            int a = w[0];
            int b = w[1];
            
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        int cnt = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        cnt++;
        visit[1] = true;
        
        while (!queue.isEmpty()) {
            int value = queue.poll();
            
            for (int neighbor : graph.get(value)) {
                if (visit[neighbor]) {
                    continue;
                }
                queue.offer(neighbor);
                cnt++;
                visit[neighbor] = true;
            }
        }
        
        int tmp = Math.abs(cnt - (n - cnt));
        answer = Math.min(answer, tmp);
    }
    
}