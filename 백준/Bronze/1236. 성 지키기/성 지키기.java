import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        boolean[] rowVisit = new boolean[N];
        Arrays.fill(rowVisit,false);
        boolean[] colVisit = new boolean[M];
        Arrays.fill(colVisit, false);

        for(int i=0; i<N; i++) {
            char[] x = br.readLine().toCharArray();
            for(int j=0; j<M; j++) {
                if(x[j] == 'X') {
                    rowVisit[i] = true;
                    colVisit[j] = true;
                }
            }
        }

        int rowCount = 0;
        for(int i=0; i<N; i++) {
            if(!rowVisit[i]) {
                rowCount++;
            }
        }

        int colCount = 0;
        for(int i=0; i<M; i++) {
            if(!colVisit[i]) {
                colCount++;
            }
        }

        int answer = (rowCount>colCount) ? rowCount : colCount;

        System.out.print(answer);
    }
}