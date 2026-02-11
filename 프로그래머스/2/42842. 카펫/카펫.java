class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int w = yellow;
        int h = 1;
        
        while (true) {
            if ((w+2) * (h+2) - w*h == brown) {
                answer[0] = w+2;
                answer[1] = h+2;
                break;
            }
            
            w--;
            while (yellow % w != 0) {
                w--;
            }
            h = yellow / w;
        }
        
        return answer;
    }
}