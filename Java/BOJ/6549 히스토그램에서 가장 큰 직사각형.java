import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static long[] height;
	static long result;
	static Stack<Integer> stack = new Stack<>();
	
	static void compare(long N) {
		long h = height[stack.peek()];
		stack.pop();
		long x = N;
		if (!stack.isEmpty()) {
			x = (N-1 - stack.peek());
		}
		result = Math.max(result, x*h);
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
        	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        	int n = Integer.parseInt(st.nextToken());
        	if (n == 0) {
        		break;
        	}
        	int i = 0;
        	height = new long[n];
        	result = 0;
        	while(st.hasMoreTokens()) {
        		height[i] = Long.parseLong(st.nextToken());
        		i++;
        	}
        	
        	for (int j = 0 ; j < n; j++) {
        		while(!stack.isEmpty() && height[stack.peek()] > height[j]) {
        			compare(j);
        		}
        		stack.add(j);
        	}
        	while (!stack.isEmpty()) {
        		compare(n);
        	}
        	System.out.println(result);
        }
    }
}