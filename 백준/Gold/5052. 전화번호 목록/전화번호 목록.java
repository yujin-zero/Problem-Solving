import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int testCase = Integer.parseInt(br.readLine());

        for(int t=0; t<testCase; t++) {
            int N = Integer.parseInt(br.readLine());
            List<String> number = new ArrayList<>();
            for(int nn=0; nn<N; nn++) {
                String x = br.readLine();
                number.add(x);
            }

            Collections.sort(number);

           int tmp = 0;
           for(int i=0; i<N-1; i++) {
               if(number.get(i+1).startsWith(number.get(i))) {
                    tmp = 1;
                    break;
               }
           }

            if(tmp==0) {
                sb.append("YES").append("\n");
            }else{
                sb.append("NO").append("\n");
            }
        }

        System.out.print(sb.toString().trim());
    }
}