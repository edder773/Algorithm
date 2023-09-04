import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] x = br.readLine().toCharArray();
        char[] M = br.readLine().toCharArray();
        int m = M.length;
        Stack<Character> stack = new Stack<>();

        for (char c : x) {
            stack.push(c);
            if (stack.size() >= m) {
                boolean isMatch = true;
                for (int i = 0; i < m; i++) {
                    if (stack.get(stack.size() - m + i) != M[i]) {
                        isMatch = false;
                        break;
                    }
                }
                if (isMatch) {
                    for (int i = 0; i < m; i++) {
                        stack.pop();
                    }
                }
            }
        }

        if (!stack.isEmpty()) {
            StringBuilder result = new StringBuilder();
            for (char c : stack) {
                result.append(c);
            }
            System.out.println(result.toString());
        } else {
            System.out.println("FRULA");
        }
    }
}