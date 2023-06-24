import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int T = Integer.parseInt(br.readLine());
    	for (int m = 0; m < T; m++){
    		Stack <Character> stack = new Stack<>();
    		String x = br.readLine();
    		for (int i = 0; i < x.length(); i++) {
    			char l = x.charAt(i);
    			stack.push(l);
    			if (stack.size() >= 2 && stack.peek() == ')' && stack.get(stack.size() -2 ) == '(') {
    				stack.pop();
    				stack.pop();
    			}
    		}
    		if (stack.empty()) {
    			System.out.println("YES");
    		}
    		else {
    			System.out.println("NO");
    		}
    	}
	}
}