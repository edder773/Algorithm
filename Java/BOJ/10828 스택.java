import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	Stack<Integer> stack = new Stack<>(); 
    	for (int i = 0; i < N; i++) {
    		List<String> x = new ArrayList<>();
    		StringTokenizer st = new StringTokenizer(br.readLine()," ");
    		while(st.hasMoreTokens()) {
    			x.add(st.nextToken());
    		}

	    	if (x.get(0).equals("push")) {
	    		stack.push(Integer.parseInt(x.get(1)));
	    	}
	    	else if(x.get(0).equals("pop")) {
	    		if (stack.size() > 0) {
	    			System.out.println(stack.pop());
	    		}
	    		else {
	    			System.out.println(-1);
	    		}
	    	}
	    	else if(x.get(0).equals("size")) {
	    		System.out.println(stack.size());
	    	}
	    	else if(x.get(0).equals("empty")) {
	    		if(stack.empty()) {
	    			System.out.println(1);
	    		}
	    		else {
	    			System.out.println(0);
	    		}
	    	}
	    	else if(x.get(0).equals("top")) {
	    		if(stack.empty()) {
	    			System.out.println(-1);
	    		}
	    		else {
	    			System.out.println(stack.peek());
	    		}
	    	}
    	}
	}
}