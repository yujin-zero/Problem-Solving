import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int testCase = Integer.parseInt(br.readLine());

        for(int t=0; t<testCase; t++) {
            int n = Integer.parseInt(br.readLine());
            String[] home = br.readLine().split(" ");
            int homeX = Integer.parseInt(home[0]);
            int homeY = Integer.parseInt(home[1]);

            int[][] convenience = new int[n][2];
            boolean[] visit = new boolean[n];
            Arrays.fill(visit, false);
            for (int i = 0; i < n; i++) {
                String[] input = br.readLine().split(" ");
                convenience[i][0] = Integer.parseInt(input[0]);
                convenience[i][1] = Integer.parseInt(input[1]);
            }

            String[] festival = br.readLine().split(" ");
            int festivalX = Integer.parseInt(festival[0]);
            int festivalY = Integer.parseInt(festival[1]);

            int tmp = Math.abs(homeX-festivalX) + Math.abs(homeY-festivalY);
            if(tmp <= 1000) {
                sb.append("happy").append("\n");
                continue;
            }

            Queue<Integer> queue = new LinkedList<>();

            for (int i = 0; i < n; i++) {
                int dis = Math.abs(homeX - convenience[i][0]) + Math.abs(homeY - convenience[i][1]);
                if (dis <= 1000) {
                    visit[i] = true;
                    queue.add(i);
                }
            }

            while(true){
                if(queue.isEmpty()){
                    sb.append("sad").append("\n");
                    break;
                }

                int nowIndex = queue.poll();

                int dis2 = Math.abs(convenience[nowIndex][0] - festivalX) + Math.abs(convenience[nowIndex][1] - festivalY);
                if(dis2 <= 1000) {
                    sb.append("happy").append("\n");
                    break;
                }

                for(int i=0; i<n; i++) {
                    if(visit[i]){
                        continue;
                    }
                    int dis = Math.abs(convenience[nowIndex][0] - convenience[i][0]) + Math.abs(convenience[nowIndex][1] - convenience[i][1]);
                    if(dis <= 1000) {
                        visit[i] = true;
                        queue.add(i);
                    }
                }


            }

        }

        System.out.print(sb.toString().trim());
    }
}