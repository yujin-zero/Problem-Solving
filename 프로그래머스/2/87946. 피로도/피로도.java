class Solution {
    int answer = -1;
    boolean[] visit;
    
    public int solution(int k, int[][] dungeons) {
        int n = dungeons.length;
        visit = new boolean[n];
        
        dfs(k, dungeons, 0, n);

        return answer;
    }
    
    public void dfs(int k, int[][] dungeons, int depth, int n) {
        answer = Math.max(answer, depth);
        for (int i=0; i<n; i++) {
            if (k < dungeons[i][0] || visit[i]) {
                continue;
            }
            visit[i] = true;
            dfs(k - dungeons[i][1], dungeons, depth+1, n);
            visit[i] = false;
        }
        return;
    }
}