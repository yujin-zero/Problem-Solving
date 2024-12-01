import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main {
    static int mod = 1000000007;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int D = Integer.parseInt(br.readLine());

        // 인접행렬 만들기
        long[][] matrix = new long[8][8];

        // 초기화
        for(int i=0; i<8; i++)
            Arrays.fill(matrix[i],0);
        matrix[0][1] = matrix[0][2] = 1;
        matrix[1][0] = matrix[1][2] = matrix[1][3] = 1;
        matrix[2][0] = matrix[2][1] = matrix[2][3] = matrix[2][5] = 1;
        matrix[3][1] = matrix[3][2] = matrix[3][4] = matrix[3][5] = 1;
        matrix[4][3] = matrix[4][5] = matrix[4][6] = 1;
        matrix[5][2] = matrix[5][3] = matrix[5][4] = matrix[5][7] = 1;
        matrix[6][4] = matrix[6][7] = 1;
        matrix[7][5] = matrix[7][6] = 1;

        long[][] answer = divid(D,matrix);
        System.out.print(answer[0][0]);

    }

    // 분할정복
    public static long[][] divid(int cnt, long[][] A) {
        if(cnt == 1) {
            return A;
        }
        if(cnt % 2 == 0) {
            long[][] tmp = divid(cnt/2, A);
            return multiMatrix(tmp,tmp);
        } else {
            long[][] tmp = divid(cnt-1, A);
            return multiMatrix(tmp, A);
        }
    }

    // 행렬의 곱
    public static long[][] multiMatrix(long[][] A, long[][] B) {
        long[][] result = new long [8][8];
        for(int i=0; i<8; i++)
            Arrays.fill(result[i],0);

        for(int i=0; i<8; i++) {
            for(int j=0; j<8; j++) {
                long tmp = 0;
                for(int k=0; k<8; k++) {
                    tmp += A[i][k] * B[k][j];
                }
                result[i][j] = tmp % mod;
            }
        }

        return result;
    }
}