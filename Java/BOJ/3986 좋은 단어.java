import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        for (int i = 0; i < N; i++) {
        	String S = br.readLine();
        	Stack<Character> stack = new Stack<>();
        	for (int j = 0 ; j < S.length(); j++) {
        		if(stack.isEmpty()){
        			stack.push(S.charAt(j));
        		}
        		else if (stack.peek() == S.charAt(j)) {
        			stack.pop();
        		}
        		else {
        			stack.add(S.charAt(j));
        		}
        	}
        	if (stack.isEmpty()) {
        		result ++;
        	}
        }
        System.out.println(result);
    }
}