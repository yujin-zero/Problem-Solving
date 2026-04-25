import java.util.*;

class Solution {
    public String solution(String number, int k) {
        String result = "";
        StringBuilder answer = new StringBuilder();
        
        int numberLen = number.length();
        int n = numberLen - k;
        // System.out.println(n);
        
        int left = 0;
        int right = numberLen - n; // left부터 right 사이에서 가장 큰 수 찾기
        
        while (true) {
            if (right > numberLen-1) {
                break;
            }
            
            int tmpMax = -1;
            int tmpIdx = -1;    
            for (int i=left; i<right+1; i++) {
                int tmp = number.charAt(i);
                if (tmp > tmpMax) {
                    tmpMax = tmp;
                    tmpIdx = i; 
                }
            }
            answer.append(number.charAt(tmpIdx));
            left = tmpIdx + 1;
            right++;
        }
        
        return answer.toString();
    }
}