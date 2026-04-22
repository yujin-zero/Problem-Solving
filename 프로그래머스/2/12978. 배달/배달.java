class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        
        int[][] distance = new int[N+1][N+1];
        for (int i=0; i<N+1; i++) {
            for (int j=0; j<N+1; j++) {
                distance[i][j] = 1000000;
            }
        }
        for (int i=1; i<N+1; i++) {
            distance[i][i] = 0;
        }
        
        int roadCnt = road.length;
        for (int i=0; i<roadCnt; i++) {
            int a = road[i][0];
            int b = road[i][1];
            int c = road[i][2];
            
            if (distance[a][b] > c) {
                distance[a][b] = c;
                distance[b][a] = c;
            }
        }
        
        for (int k=1; k<N+1; k++) {
            for (int i=1; i<N+1; i++) {
                for (int j=1; j<N+1; j++) {
                    if (distance[i][j] > distance[i][k] + distance[k][j]) {
                        distance[i][j] = distance[i][k] + distance[k][j];
                        distance[j][i] = distance[i][j];
                    }
                }
            }
        }
        
        for (int i=1; i<N+1; i++) {
            if (distance[1][i] <= K) {
                answer++;
            }
        }
            
        return answer;
    }
}