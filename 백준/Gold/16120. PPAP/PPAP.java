import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] input = br.readLine().toCharArray();
        int N = input.length;

        Stack<Character> stack = new Stack<>();
        for(int i=0; i<N; i++) {
            char currentChar = input[i];
            if(currentChar == 'A') {
                stack.push('A');
            }else {
                int size = stack.size();
                if(size < 3) {
                    stack.push('P');
                }else {
                    if(stack.elementAt(size-3) == 'P' && stack.elementAt(size-2) == 'P'
                        && stack.elementAt(size-1) == 'A' ) {
                        stack.pop();
                        stack.pop();
                    } else {
                        stack.push('P');
                    }
                }
            }
        }

        if (stack.size() == 1 ) {
            if(stack.get(0)=='P') {
                System.out.print("PPAP");
            } else{
                System.out.print("NP");
            }
        }else{
            System.out.print("NP");
        }

    }
}