import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < N; t++) {
        	int[] x = new int[2];
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	int i = 0;
        	while(st.hasMoreTokens()) {
        		x[i] = Integer.parseInt(st.nextToken());
        		i++;
        	}
        	if (x[0] == 1) {
        		stack.add(x[1]);
        	}
        	else if (x[0] == 2) {
        		if(stack.isEmpty()) {
        			sb.append(-1).append("\n");
        		}
        		else {
        			sb.append(stack.pop()).append("\n");
        		}
        	}
        	else if (x[0] == 3) {
        		sb.append(stack.size()).append("\n");
        	}
        	else if (x[0] == 4) {
        		if(stack.isEmpty()) {
        			sb.append(1).append("\n");
        		}
        		else {
        			sb.append(0).append("\n");
        		}
        	}
        	else if (x[0] == 5){
        		if(stack.isEmpty()) {
        			sb.append(-1).append("\n");
        		}
        		else {
        			sb.append(stack.peek()).append("\n");
        		}
        	}
        }
        System.out.println(sb);
    }
}