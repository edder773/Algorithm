import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int K = Integer.parseInt(br.readLine());
    	Stack <Integer> stack = new Stack<>();
    	int result = 0;
    	for(int i = 0; i < K; i++) {
    		int num = Integer.parseInt(br.readLine());
    		if (num == 0) {
    			result -= stack.pop();
    		}
    		else {
    			stack.push(num);
    			result += num;
    		}
    	}
    	System.out.println(result);
	}
}