import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
        	StringBuilder sb = new StringBuilder();
        	sb.append("[");
        	String p = br.readLine();
        	int n = Integer.parseInt(br.readLine());
        	Deque<Integer> queue = new LinkedList<>();
        	String S = br.readLine();
        	StringTokenizer st = new StringTokenizer(S.substring(1,S.length()-1),",");
        	for (int i = 0; i < n; i++) {
        		queue.add(Integer.parseInt(st.nextToken()));
        	}
        	int cnt = 0;
        	int flag = 1;
        	for (char x: p.toCharArray()) {
        		if (x == 'R') {
        			cnt += 1;
        		}
        		else {
        			if (queue.isEmpty()) {
        				sb = new StringBuilder();
        				sb.append("error");
        				flag = 0;
        				break;
        			}
        			if (cnt % 2 == 0) {
        				queue.pollFirst();
        			}
        			else {
        				queue.pollLast();
        			}
        		}
        	}
        	if (flag == 1) {
        		if (cnt % 2 == 1) {
        			while(queue.size() > 1) {
        				sb.append(queue.pollLast()).append(",");
        			}
        			if (queue.isEmpty()) {
        				sb.append("]");
        			}
        			else {
        				sb.append(queue.pollLast()).append("]");    				        				
        			}
        		}
        		else {
        			while(queue.size() > 1) {
        				sb.append(queue.pollFirst()).append(",");
        			}
        			if (queue.isEmpty()) {
        				sb.append("]");
        			}
        			else {
        				sb.append(queue.pollFirst()).append("]");    				        				
        			} 				
        		}    		
        	}
    		System.out.println(sb);
        }
    }
}