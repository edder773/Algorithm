import java.io.*;
import java.util.*;

public class Main {    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque <Integer> queue = new ArrayDeque<>();
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int[] queuestack = new int[N];
        for (int i = 0; i < N; i ++) {
        	queuestack[i] = Integer.parseInt(st.nextToken());
        }
        int[] num = new int[N];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0 ; i < N; i++) {
        	num[i] = Integer.parseInt(st.nextToken());
        }
        int M = Integer.parseInt(br.readLine());
        int[] insert = new int[M];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0 ; i < M; i++) {
        	insert[i] = Integer.parseInt(st.nextToken());
        }
        for(int i = 0 ; i< N; i ++) {
        	if (queuestack[i] == 0) {
        		queue.addFirst(num[i]);
        	}
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++){
        	queue.addLast(insert[i]);
        	sb.append(queue.pollFirst()).append(' ');
        }
        System.out.println(sb);
    }
}