import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        List<Integer> peopleList = new ArrayList<>();
        int N = people.length;
        for (int i=0; i<N; i++) {
            peopleList.add(people[i]);
        }
        peopleList.sort((a,b) -> a-b);
        
        int left = 0;
        int right = N-1;
        
        while (true) {
            if (left == right) {
                answer++;
                break;
            } else if (left > right) {
                break;
            }
            
            if (peopleList.get(left) + peopleList.get(right) <= limit) {
                answer++;
                left++;
                right--;
            } else {
                answer++;
                right--;
            }
        }
        
        
        return answer;
    }
}