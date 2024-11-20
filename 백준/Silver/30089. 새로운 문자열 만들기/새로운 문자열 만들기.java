import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for(int t=0; t<T; t++) {
            char[] input = br.readLine().toCharArray();
            List<Character> addList = new ArrayList<>();
            char lastChar = input[input.length-1];

            for(int i=0; i<input.length-1; i++) {
                char nowChar = input[i];

                if(nowChar != lastChar) {
                    addList.add(nowChar);
                    continue;
                }

                int beginIndex = i;
                int lastIndex = input.length - 1;

                boolean check = true;
                while(beginIndex < lastIndex) {
                    if(input[beginIndex] != input[lastIndex]) {
                        check = false;
                        break;
                    }
                    beginIndex++;
                    lastIndex--;
                }

                if(!check) {
                    addList.add(nowChar);
                } else {
                    break;
                }
            }

            sb.append(input);
            for(int i=addList.size()-1; i>-1; i--) {
                sb.append(addList.get(i));
            }
            sb.append("\n");
        }

        System.out.print(sb.toString().trim());

    }
}
