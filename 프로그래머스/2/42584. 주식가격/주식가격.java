class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        for (int i=0; i<prices.length; i++) {
            int tmp = 0;
            int current = prices[i];
            for (int j=i+1; j<prices.length; j++) {
                int next = prices[j];
                tmp++;
                if (current > next) {
                    break;
                }
            }
            answer[i] = tmp;
        }
        
        return answer;
    }
}