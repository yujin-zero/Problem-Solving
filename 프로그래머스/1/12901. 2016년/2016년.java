class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int[] dayCnt = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int tmp = 5; // 금요일
        int currentMonth = 1;
        int currentDay = 1;
        String[] days = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        
        
        while (true) {
            if (currentMonth == a && currentDay == b) {
                break;
            }
            
            int endDay = dayCnt[currentMonth];
            
            currentDay++;
            if (currentDay > endDay) {
                currentMonth++;
                currentDay = 1;
            }
            
            tmp++;
            if (tmp >= 7) {
                tmp = 0;
            }
        }        
        answer = days[tmp];
        
        return answer;
    }
}