import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        
        HashMap<String, Integer> hm = new HashMap<>();
        int N = genres.length;
        for (int i=0; i<N; i++) {
            if (hm.containsKey(genres[i])) {
                int tmp = hm.get(genres[i]);
                hm.put(genres[i], tmp + plays[i]);
            } else {
                hm.put(genres[i], plays[i]);
            }
        }
        
        int[][] playList = new int[N][4];
        for (int i=0; i<N; i++) {
            playList[i][0] = hm.get(genres[i]);
            playList[i][1] = plays[i];
            playList[i][2] = i;
        }
        
        Arrays.sort(playList, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            } else {
                return b[0] - a[0];
            }
        });
        
        List<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> hmCnt = new HashMap<>();
        for (int i=0; i<N; i++) {
            int idx = playList[i][2];
            String currentGenre = genres[idx];
            if (hmCnt.containsKey(currentGenre)) {
                int tmp = hmCnt.get(currentGenre); 
                hmCnt.put(currentGenre, tmp + 1);
            } else {
                hmCnt.put(currentGenre, 1);
            }
            
            if (hmCnt.get(currentGenre) > 2) {
                continue;
            }
            answer.add(idx);
        }
        
        int[] result = new int[answer.size()];
        for (int i=0; i<answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}