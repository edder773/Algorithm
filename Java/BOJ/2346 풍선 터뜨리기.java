import java.io.*;
import java.util.*;

public class Main {    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque <int[]> queue = new ArrayDeque<>();
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N+1; i++) {
        	int n = Integer.parseInt(st.nextToken());
        	queue.add(new int[] {i, n});
        }
        while(true) {
        	int[] x = queue.poll();
        	sb.append(x[0]).append(" ");
        	int num = x[1];
        	if (queue.isEmpty()) {
        		break;
        	}
        	if (num > 0) {
        		for(int i = 0 ; i < num - 1; i++) {
        			queue.offerLast(queue.pollFirst());
        		}
        	}
        	else {
        		for(int i = 0 ; i < -num; i++) {
        			queue.offerFirst(queue.pollLast());
        		}
        	}
        }
        System.out.println(sb);
    }
}