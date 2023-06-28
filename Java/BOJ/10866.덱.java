import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque<String> queue = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            List<String> x = new ArrayList<>();
            while (st.hasMoreTokens()) {
                x.add(st.nextToken());
            }
            if (x.get(0).equals("push_front")){
            	queue.push(x.get(1));
            }
            else if (x.get(0).equals("push_back")) {
            	queue.addLast(x.get(1));
            }
            else if (x.get(0).equals("pop_front")) {
            	if (queue.isEmpty()) {
            		sb.append(-1).append("\n");
            	}
            	else {
            		sb.append(queue.removeFirst()).append("\n");            		
            	}
            }
            else if (x.get(0).equals("pop_back")) {
            	if (queue.isEmpty()) {
            		sb.append(-1).append("\n");
            	}
            	else {
            		sb.append(queue.removeLast()).append("\n");            		
            	}
            }
            else if (x.get(0).equals("size")) {
            	sb.append(queue.size()).append("\n");
            }
            else if (x.get(0).equals("empty")) {
            	if (queue.isEmpty()) {
            		sb.append(1).append("\n");
            	}
            	else {
            		sb.append(0).append("\n");
            	}
            }
            else if (x.get(0).equals("front")) {
            	if (queue.isEmpty()) {
            		sb.append(-1).append("\n");
            	}
            	else {
            		sb.append(queue.getFirst()).append("\n");            		
            	}
            }
            else if (x.get(0).equals("back")) {
            	if (queue.isEmpty()) {
            		sb.append(-1).append("\n");
            	}
            	else {
            		sb.append(queue.getLast()).append("\n");            		
            	}
            }
        }
        System.out.println(sb);
    }
}