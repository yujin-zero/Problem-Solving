import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int input= sc.nextInt();
        int i = 2;

        while (true) {
            if (i > input) {
                break;
            }

            if (input % i == 0 ){
                System.out.println(i);
                input /= i;
            } else {
                i++;
            }
        }
    }
}
