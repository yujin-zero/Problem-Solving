import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> intList = new ArrayList<>();
        int pre = -1;
        for (int a : arr) {
            if (a != pre) {
                intList.add(a);
            }
            pre = a;
        }
        
        int[] answer = new int[intList.size()];
        for (int i=0; i<intList.size(); i++) {
            answer[i] = intList.get(i);
        }
        
        return answer;
    }
}