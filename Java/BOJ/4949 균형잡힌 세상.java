import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	while (true) {
    		String S = br.readLine();
    		if (S.equals(".")) {
    			break;
    		}
    		Stack <Character> stack = new Stack<>();
    		for (int i = 0; i < S.length(); i++) {
    			char x = S.charAt(i);
    			if (x == '(' || x == ')' || x == '[' || x == ']') {
    				stack.push(x);
    			}
    			int m = stack.size();
    			if(m >= 2) {
    				if (((stack.peek() == ')' && stack.get(m-2) == '(')) || (stack.peek() == ']' && stack.get(m-2) == '[')) {
    					stack.pop();
    					stack.pop();
    				}    				
    			}
    		}
    		if (stack.empty()) {
    			System.out.println("yes");
    		}
    		else {
    			System.out.println("no");
    		}
    	}
	}
}