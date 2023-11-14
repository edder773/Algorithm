import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String S = br.readLine();
        int result = 0;
        Stack<Character> r = new Stack<>();
        Stack<Character> k = new Stack<>();

        for (char i : S.toCharArray()) {
            if (Character.isDigit(i)) {
                result += 1;
            } else if (i == 'L') {
                r.push(i);
            } else if (i == 'R') {
                if (!r.isEmpty() && r.peek() == 'L') {
                    r.pop();
                    result += 1;
                } else {
                    break;
                }
            } else if (i == 'S') {
                k.push(i);
            } else if (i == 'K') {
                if (!k.isEmpty() && k.peek() == 'S') {
                    k.pop();
                    result += 1;
                } else {
                    break;
                }
            }
        }

        System.out.println(result);
    }
}