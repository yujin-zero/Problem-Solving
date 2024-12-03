import java.io.*;
import java.util.*;

class Cost {
    int l, r, c;
    public Cost(int l, int r, int c) {
        this.l = l;
        this.r = r;
        this.c = c;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 입력 처리
        int N = Integer.parseInt(br.readLine());
        int[] A = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int M = Integer.parseInt(br.readLine());
        List<Cost> costs = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken()) - 1;
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken());
            costs.add(new Cost(l, r, c));
        }

        // 목표 상태 계산
        int[] sortedA = Arrays.copyOf(A, N);
        Arrays.sort(sortedA);
        StringBuilder targetBuilder = new StringBuilder();
        for (int num : sortedA) {
            targetBuilder.append(num == 10 ? 0 : num);
        }
        String target = targetBuilder.toString();

        // 초기 상태 계산
        StringBuilder startBuilder = new StringBuilder();
        for (int num : A) {
            startBuilder.append(num == 10 ? 0 : num);
        }
        String start = startBuilder.toString();

        // 다익스트라 준비
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        Map<String, Integer> dp = new HashMap<>();
        dp.put(start, 0);
        pq.add(new int[]{0, Integer.parseInt(start)});

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int nowCost = current[0];
            String nowNode = String.format("%0" + N + "d", current[1]); // 자릿수 맞추기

            if (nowCost > dp.getOrDefault(nowNode, Integer.MAX_VALUE)) {
                continue;
            }

            for (Cost cost : costs) {
                char[] nextNode = nowNode.toCharArray();
                char temp = nextNode[cost.l];
                nextNode[cost.l] = nextNode[cost.r];
                nextNode[cost.r] = temp;

                String nextNodeStr = new String(nextNode);
                int newCost = nowCost + cost.c;

                if (newCost < dp.getOrDefault(nextNodeStr, Integer.MAX_VALUE)) {
                    dp.put(nextNodeStr, newCost);
                    pq.add(new int[]{newCost, Integer.parseInt(nextNodeStr)});
                }
            }
        }

        // 결과 출력
        if (dp.getOrDefault(target, Integer.MAX_VALUE) == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(dp.get(target));
        }
    }
}
