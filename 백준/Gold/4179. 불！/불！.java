import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        char[][] graph = new char[N][M];
        int[] dx = {0,0,-1,1};
        int[] dy = {-1,1,0,0};

        boolean[][] visitJ = new boolean[N][M];
        for(int i=0; i<N; i++) {
            Arrays.fill(visitJ[i],false);
        }
        boolean[][] visitF = new boolean[N][M];
        for(int i=0; i<N; i++) {
            Arrays.fill(visitF[i],false);
        }

        Queue<int[]> queueJ = new LinkedList<>();
        Queue<int[]> queueF = new LinkedList<>();

        for(int i=0; i<N; i++) {
            graph[i] = br.readLine().toCharArray();

            for(int j=0; j<M; j++) {
                if(graph[i][j]=='J') {
                    queueJ.add(new int[]{i,j});
                    visitJ[i][j] = true;
                }else if(graph[i][j] == 'F'){
                    queueF.add(new int[]{i,j});
                    visitF[i][j] = true;
                }
            }
        }

        int minute = 0;
        boolean game = true;
        boolean checkOut = false;
        while(game) {
           minute++;

            // 불 움직이기
            Queue<int[]> newQueueF = new LinkedList<>();
            while(!queueF.isEmpty() && game) {
                int[] pair = queueF.poll();
                int x = pair[0];
                int y = pair[1];

                for(int k=0; k<4; k++) {
                    int newX = x + dx[k];
                    int newY = y + dy[k];

                    if(!(0 <= newX && newX < N && 0 <= newY && newY < M)) {
                        continue;
                    }

                    if(graph[newX][newY] != '#' && !visitF[newX][newY]) {
                        newQueueF.add(new int[]{newX, newY});
                        visitF[newX][newY] = true;
                        graph[newX][newY] = 'F';
                    }
                }
            }
            queueF = newQueueF;

           // 지훈이 움직이기 , 지훈이가 탈출하면 gameover
            Queue<int[]> newQueueJ = new LinkedList<>();
            while(!queueJ.isEmpty() && game){
                int[] pair = queueJ.poll();
                int x = pair[0];
                int y = pair[1];

                for(int k=0; k<4; k++) {
                    int newX = x + dx[k];
                    int newY = y + dy[k];

                    if(!(0 <= newX && newX < N && 0 <= newY && newY < M) ) {
                        game = false;
//                        System.out.println("newX : "+newX + " newY : "+newY);
                        break;
                    }

                    if(graph[newX][newY] == '.' && !visitJ[newX][newY]) {
                        newQueueJ.add(new int[]{newX, newY});
                        visitJ[newX][newY] = true;
                    }
                }
            }
            queueJ = newQueueJ;



            // 지훈이가 다 죽었으면 gameover
            if(newQueueJ.isEmpty() && game) {
                game = false;
                checkOut = true;
            }
        }

        if(checkOut) {
            System.out.print("IMPOSSIBLE");
        }else{
            System.out.print(minute);
        }


    }
}