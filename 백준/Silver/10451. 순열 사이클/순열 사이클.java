import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for(int testcase=0; testcase<T; testcase++) {
            int N = Integer.parseInt(br.readLine());
            String[] input = br.readLine().split(" "); // 입력 이런 식으로 하는 게 최선인가
            List<Integer> graph = new ArrayList<>();
            graph.add(-1);
            for(String s : input) {
                graph.add(Integer.parseInt(s));
            }
//            System.out.println(graph);

            int answer = 0;
            Boolean[] visit = new Boolean[N+1];
            Arrays.fill(visit, false);


            Queue<Integer> queue = new LinkedList<>(); // 근데 queue 가 그냥 리스트랑 뭔 차이지

            queue.add(1);
            visit[1] = true;

            while(!queue.isEmpty()) {
                int nowNode = queue.poll();
                int nextNode = graph.get(nowNode);
//                System.out.println("nowNode : " + nowNode + "nextNode : " + nextNode);

                if (visit[nextNode]) {

                    answer++;
                    // 다음 노드 찾기 방문 안한
                    for (int i=1; i<N+1; i++) {
                        if(!visit[i]){
                            queue.add(i);
                            visit[i] = true;
                            break;
                        }
                    }
                } else {
                    queue.add(nextNode);
                    visit[nextNode] = true;
                }

            }

            sb.append(answer).append("\n");
        }

        System.out.print(sb.toString().trim());
    }

}