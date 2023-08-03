import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int[] student = new int[N];
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < N; i ++) {
        	student[i] = Integer.parseInt(st.nextToken());
        }
        int num = 1;
        for (int i = 0; i < N; i++) {
        	if (student[i] == num) {
        		num ++;
        	}
        	else if(!stack.isEmpty() && stack.peek() == num) {
        		stack.pop();
        		num ++;
        	}
        	else {
        		stack.add(student[i]);
        	}
        	while (!stack.isEmpty()) {
        		if (stack.peek() == num) {
        			num ++;
        			stack.pop();
        		}
        		else {
        			break;
        		}
        	}
        }
        if (stack.isEmpty()) {
        	System.out.println("Nice");
        }
        else {
        	System.out.println("Sad");
        }
    }
}