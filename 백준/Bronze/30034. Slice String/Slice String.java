import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int charSplitCount = Integer.parseInt(br.readLine());
        List<Character> charSplits = new ArrayList<>();
        char[] inputCharSplit = br.readLine().toCharArray();
        for(char c : inputCharSplit) {
            charSplits.add(c);
        }

        int intSplitCount = Integer.parseInt(br.readLine());
        List<Character> intSplits = new ArrayList<>();
        char[] inputIntSplit = br.readLine().toCharArray();
        for(char c : inputIntSplit) {
            intSplits.add(c);
        }

        int mergeCount = Integer.parseInt(br.readLine());
        List<Character> merges = new ArrayList<>();
        char[] inputMerge = br.readLine().toCharArray();
        for(char c : inputMerge) {
            merges.add(c);
        }

        int stringCount = Integer.parseInt(br.readLine());
        char[] string = br.readLine().toCharArray();

        StringBuilder output = new StringBuilder();
        boolean breakLine = true;
        for(char c : string) {
            if((charSplits.contains(c) || intSplits.contains(c)) && !merges.contains(c) || c==' '){
                if(breakLine) {
                    output.append("\n");
                    breakLine = false;
                }

            }else {
                output.append(c);
                breakLine = true;
            }
        }

        System.out.print(output.toString().trim());
    }
}