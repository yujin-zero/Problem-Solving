class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int maxW = -1;
        int maxH = -1;
        
        for (int[] s : sizes) {
            int w = s[0];
            int h = s[1];
            if (h > w) {
                int tmp = w;
                w = h;
                h = tmp;
            }
            if (w > maxW) {
                maxW = w;
            }
            if (h > maxH) {
                maxH = h;
            }
        }
        answer = maxW * maxH;
        
        return answer;
    }
}