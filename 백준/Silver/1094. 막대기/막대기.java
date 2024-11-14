import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        list.add(64);

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum;

        while (true) {
            sum = list.stream().mapToInt(Integer::intValue).sum();
            if (n == sum) {
                break;
            }
            int smallInt = list.removeLast();

            list.add(smallInt/2);
            if (list.stream().mapToInt(Integer::intValue).sum() < n )
                list.add(smallInt/2);

        }

        System.out.println(list.size());

    }
}
