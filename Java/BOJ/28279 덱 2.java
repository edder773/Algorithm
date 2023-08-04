import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque <Integer> queue = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for (int t = 0 ; t < N; t++) {
        	int[] x = new int[2];
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	int i = 0;
        	while (st.hasMoreTokens()) {
        		x[i] = Integer.parseInt(st.nextToken());
        		i++;
        	}
        	if(x[0] == 1) {
        		queue.addFirst(x[1]);
        	}
        	else if(x[0] == 2) {
        		queue.addLast(x[1]);
        	}
        	else if(x[0] == 3) {
        		if (queue.isEmpty()) {
        			sb.append(-1).append("\n");
        		}
        		else {
        			sb.append(queue.pollFirst()).append("\n");
        		}
        	}
        	else if(x[0] == 4) {
        		if (queue.isEmpty()) {
        			sb.append(-1).append("\n");
        		}
        		else {
        			sb.append(queue.pollLast()).append("\n");
        		}
        	}
        	else if(x[0] == 5) {
        		sb.append(queue.size()).append("\n");
        	}
        	else if(x[0] == 6) {
        		if (queue.isEmpty()) {
        			sb.append(1).append("\n");
        		}
        		else {
        			sb.append(0).append("\n");
        		}
        	}
        	else if(x[0] == 7) {
        		if (queue.isEmpty()) {
        			sb.append(-1).append("\n");
        		}
        		else {
        			sb.append(queue.getFirst()).append("\n");
        		}
        	}
        	else if(x[0] == 8) {
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