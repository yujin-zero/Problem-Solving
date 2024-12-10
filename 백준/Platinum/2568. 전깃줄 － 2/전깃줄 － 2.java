import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[][] input = new int[N][2];
        HashMap<Integer, Integer> mapB = new HashMap<>();
        StringTokenizer st;
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            input[i][0] = Integer.parseInt(st.nextToken());
            input[i][1] = Integer.parseInt(st.nextToken());
            mapB.put(input[i][1],input[i][0]);
        }
        Arrays.sort(input, Comparator.comparingInt(a -> a[0]));

        List<Integer> lis = new ArrayList<>();
        List<int[]> total = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();
        int findIdx = -1;

        for(int i=0; i<N; i++) {
            int value = input[i][1];

            if(lis.isEmpty() || lis.get(lis.size()-1) < value) {
                lis.add(value);
                total.add(new int[]{lis.size(),value});
                findIdx = lis.size();
            } else {
                int left = 0;
                int right = lis.size()-1;

                while(left <= right){
                    int mid = (left+right)/2;

                    if(lis.get(mid) > value) {
                        right = mid-1;
                    }else {
                        left = mid+1;
                    }
                }

                lis.set(left,value);
                total.add(new int[]{left+1,value});
            }
        }

        for(int i=total.size()-1; i>-1; i--) {
            int idx = total.get(i)[0];
            int num = total.get(i)[1];
            if(idx == findIdx) {
                findIdx -= 1;
            }else {
                answer.add(mapB.get(num));
            }
        }

        Collections.sort(answer);
        System.out.println(answer.size());
        for (Integer integer : answer) {
            sb.append(integer).append("\n");
        }
        System.out.print(sb.toString().trim());
    }
}
