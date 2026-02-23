import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> result = new ArrayList<>();
        String[] today_lst = today.split("\\.");
        int today_year = Integer.valueOf(today_lst[0]);
        int today_month = Integer.valueOf(today_lst[1]);
        int today_day = Integer.valueOf(today_lst[2]);
        HashMap<String, Integer> hm = new HashMap<>();
        
        for (String term : terms) {
            String[] term_lst = term.split(" ");
            String type = term_lst[0];
            int period = Integer.valueOf(term_lst[1]);
            hm.put(type, period);
        }

        int idx = 0;
        for (String privacie : privacies) {
            idx++;
            String[] privacie_lst = privacie.split(" ");
            String[] day_lst = privacie_lst[0].split("\\.");
            int p_year = Integer.valueOf(day_lst[0]);
            int p_month = Integer.valueOf(day_lst[1]);
            int p_day = Integer.valueOf(day_lst[2]);
            String t = privacie_lst[1];
            int current_period = hm.get(t);
            
            p_month += current_period;
            if (p_month > 12) {
                if (p_month % 12 == 0) {
                    p_year += p_month/12 - 1;
                    p_month = 12;
                } else {
                    p_year += p_month/12;
                    p_month %= 12;
                }
            }
            
            if (p_year > today_year) {
                continue;
            } else if (p_year < today_year) {
                result.add(idx);
                continue;
            }
            
            if (p_month > today_month) {
                continue;
            } else if (p_month < today_month) {
                result.add(idx);
                continue;
            }
            
            if (p_day <= today_day) {
                result.add(idx);
            }
        }
        
        int[] answer = new int[result.size()];
        for (int i=0; i<result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}