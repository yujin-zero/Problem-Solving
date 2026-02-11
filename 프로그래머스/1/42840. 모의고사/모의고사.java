import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[][] value = {{1,2,3,4,5}, {2,1,2,3,2,4,2,5}, {3,3,1,1,2,2,4,4,5,5}};
        int[] idx = {0,0,0};
        int[] correct = {0,0,0};
        
        for (int a : answers) {
            for (int i=0; i<3; i++) {
                if (value[i][idx[i]] == a) {
                    correct[i]++;
                }
                idx[i]++;
                if (idx[i] >= value[i].length) {
                    idx[i] = 0;
                }
            }
        }
        
        int maxCorrect = -1;
        for (int i=0; i<3; i++) {
            if (correct[i] > maxCorrect) {
                maxCorrect = correct[i];
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i=0; i<3; i++) {
            if (maxCorrect == correct[i]) {
                ans.add(i+1);
            }
        }
        int[] answer = new int[ans.size()];
        for (int i=0; i<ans.size(); i++) {
            answer[i] = ans.get(i);
        }
            
        return answer;
    }
}