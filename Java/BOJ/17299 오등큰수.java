import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] x = new int[N];
        int[] temp = new int[1000001];
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[N];
        Arrays.fill(result, -1);
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        for (int i = 0; i < N; i++) {
            x[i] = Integer.parseInt(st.nextToken());
            temp[x[i]]++;
        }

        for (int i = 0; i < N; i++) {
            while (!stack.isEmpty() && temp[x[stack.peek()]] < temp[x[i]]) {
                result[stack.pop()] = x[i];
            }
            stack.push(i);
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(result[i] + " ");
        }
        System.out.println(sb);
    }
}