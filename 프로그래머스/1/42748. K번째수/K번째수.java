import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int tmp = 0;
        
        for (int[] com : commands) {
            int i = com[0];
            int j = com[1];
            int k = com[2];
            
            List<Integer> newArray = new ArrayList<>();
            for (int x=i-1; x<j; x++) {
                newArray.add(array[x]);
            }
            
            Collections.sort(newArray);
            answer[tmp] = newArray.get(k-1);
            tmp++;
        }
        
        return answer;
    }
}