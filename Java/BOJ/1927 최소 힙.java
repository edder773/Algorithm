import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	PriorityQueue<Integer> queue = new PriorityQueue<>((a, b) -> a - b);
    	StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
            	if(queue.isEmpty()) {
            		sb.append(0).append('\n');
            	}
            	else {
            		sb.append(queue.poll()).append('\n');
            	}
            }
            else {
            	queue.add(n);
            }
        }
        System.out.println(sb);
    }
}