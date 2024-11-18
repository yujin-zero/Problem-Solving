import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;

        int N = Integer.parseInt(br.readLine());
        List<Integer> plusList = new ArrayList<>();
        List<Integer> minusList = new ArrayList<>();

        for(int i=0; i<N; i++) {
            int input = Integer.parseInt(br.readLine());
            if(input > 0 ){
                plusList.add(input);
            }else {
                minusList.add(input);
            }
        }

        Collections.sort(plusList);
        Collections.sort(minusList);

        for(int i=plusList.size()-1; i>-1; i--) {
            if(plusList.get(i) == 1) {
                answer++;
            } else {
                if(i==0) {
                    answer += plusList.get(i);
                }else{
                    int beforeNumber = plusList.get(i-1);
                    if (beforeNumber == 1 ){
                        answer += plusList.get(i);
                    }else {
                        answer += plusList.get(i) * beforeNumber;
                        i--;
                    }
                }
            }
        }

        for(int i=0; i<minusList.size(); i++) {
            if(i==minusList.size()-1) {
                answer += minusList.get(i);
            }else{
                answer += minusList.get(i) * minusList.get(i+1);
                i++;
            }
        }

        System.out.print(answer);
    }
}