import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	Stack<Integer> stack = new Stack<>();
    	StringBuilder sb = new StringBuilder();
    	int m = 1;
    	for (int i = 0; i < n; i++) {
    		int x = Integer.parseInt(br.readLine());
    		if (!stack.empty() && stack.peek() > x) {
    			sb = new StringBuilder();
    			sb.append("NO");
    			break;
    		}
    		while (true) {
    			if (!stack.empty() && stack.peek() == x) {
    				sb.append("-").append("\n");
    				stack.pop();
    				break;
    			}
    			stack.push(m);
    			sb.append("+").append("\n");
    			m++;
    			}
    	}
    	System.out.println(sb);
	}
}