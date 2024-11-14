import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] answer = new int[N];
        sc.nextLine();
//        ArrayList<Integer> leftPersonCnt = sc.next().split(' ');

        String[] input = sc.nextLine().split(" ");

        ArrayList<Integer> leftPersonCnt = new ArrayList<>();
        for (String s : input) {
            leftPersonCnt.add(Integer.parseInt(s));
        }

        for (int i=0; i<N; i++) {
            int tmp = leftPersonCnt.get(i);
            int cnt = 0;
            for (int j=0; j<N; j++) {
                if (cnt == tmp && answer[j] == 0) {
                    answer[j] = i+1;
                    break;
                }
                if (answer[j] == 0) {
                    cnt++;
                }
            }
        }

        for(int i : answer) {
            System.out.print(i + " ");
        }
    }
}
