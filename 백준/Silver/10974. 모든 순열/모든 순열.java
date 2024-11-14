import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        recursion(n, list);
    }

    public static void recursion(int n,ArrayList<Integer> numbers) {
        if (numbers.size() == n) {
            for(Integer value : numbers) {
                System.out.print(value + " ");
            }
            System.out.println();
        }

        for (int i=1; i<=n; i++) {
            if (!numbers.contains(i)) {
                numbers.add(i);
                recursion(n, numbers);
                numbers.remove(Integer.valueOf(i));
            }
        }

    }
}
