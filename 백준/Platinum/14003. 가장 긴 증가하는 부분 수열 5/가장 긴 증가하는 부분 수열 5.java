import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] input = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> lstArr = new ArrayList<>();
        List<int[]> lstTotal = new ArrayList<>();
        lstArr.add(Integer.MIN_VALUE);
        lstTotal.add(new int[] {Integer.MIN_VALUE,0});

        for(int value : input) {
            if(value > lstArr.get(lstArr.size()-1)) {
                lstArr.add(value);
                lstTotal.add(new int[] {value, lstArr.size()-1});
            } else {
                int findIdx = -1;
                int left = 0;
                int right = lstArr.size()-1;

                while(left <= right) {
                    int mid = (left+right)/2;

                    if(lstArr.get(mid) >= value) {
                        findIdx = mid;
                        right = mid-1;
                    }else {
                        left = mid +1;
                    }
                }

                lstArr.set(findIdx, value);
                lstTotal.add(new int[] {value, findIdx});
            }
        }

        List<Integer> answer = new ArrayList<>();

        int currentIdx = lstArr.size()-1;
        for(int i=lstTotal.size()-1; i>-1; i--) {
            if(currentIdx == 0 ){
                break;
            }

            if(lstTotal.get(i)[1] == currentIdx) {
                answer.add(lstTotal.get(i)[0]);
                currentIdx--;
            }
        }

        System.out.println(lstArr.size()-1);
        for(int i=answer.size()-1; i>-1; i--)
            System.out.print(answer.get(i) + " ");



    }
}