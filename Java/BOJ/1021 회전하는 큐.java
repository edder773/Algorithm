import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        LinkedList<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            queue.addLast(i);
        }
        int result = 0;
        for (int i = 0; i < M; i++) {
            int num = Integer.parseInt(st.nextToken());
            while (true) {
                if (queue.getFirst() == num) {
                    queue.pollFirst();
                    break;
                } else {
                    if (queue.indexOf(num) <= queue.size() / 2) {
                        queue.addLast(queue.pollFirst());
                        result += 1;
                    } else {
                        queue.addFirst(queue.pollLast());
                        result += 1;
                    }
                }
            }
        }
        System.out.println(result);
    }
}