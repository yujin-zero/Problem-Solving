import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        
        String[] num_lst = s.split(" ");
        List<Integer> nums = new ArrayList<>();
        for (String n : num_lst) {
            nums.add(Integer.valueOf(n));
        }
        Collections.sort(nums);
        int n = nums.size();
        answer.append(Integer.toString(nums.get(0)));
        answer.append(" ");
        answer.append(Integer.toString(nums.get(n-1)));
        
        return answer.toString();
    }
}