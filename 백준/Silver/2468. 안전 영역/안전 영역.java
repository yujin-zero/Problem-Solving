import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int heightMin = Integer.MAX_VALUE;
        int heightMax = Integer.MIN_VALUE;
        int answer = 0;

        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};


        List<List<Integer>> graph = new ArrayList<>();

        for(int i=0; i<N; i++) {
            List<Integer> g = new ArrayList<>();
            String[] input = br.readLine().split(" ");
            for(String s : input) {
                g.add(Integer.parseInt(s));
            }
            graph.add(g);

            heightMin = Math.min(heightMin, Collections.min(g));
            heightMax = Math.max(heightMax, Collections.max(g));
        }

        for(int currentHeight = heightMin; currentHeight<heightMax+1; currentHeight++) {
            int areaCount = 0;

            Queue<int[]> queue = new LinkedList<>();
            Boolean[][] visit = new Boolean[N][N];
            for(int i=0; i<N; i++) {
                Arrays.fill(visit[i],false);
            }

            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    if(visit[i][j] || graph.get(i).get(j) < currentHeight)
                        continue;

                    areaCount++;
                    queue.add(new int[]{i,j});
                    visit[i][j] = true;

                    while(!queue.isEmpty()) {
                        int[] pair = queue.poll();
                        int x = pair[0];
                        int y = pair[1];

                        for(int k=0; k<4; k++) {
                            int newX = x + dx[k];
                            int newY = y + dy[k];

                            if(!(0 <= newX && newX < N && 0 <= newY && newY < N)) {
                                continue;
                            }
                            if(!visit[newX][newY] && graph.get(newX).get(newY) >= currentHeight){
                                queue.add(new int[]{newX,newY});
                                visit[newX][newY] = true;
                            }
                        }
                    }

                }
            }

            answer = Math.max(answer, areaCount);
        }


        System.out.print(answer);
    }
}