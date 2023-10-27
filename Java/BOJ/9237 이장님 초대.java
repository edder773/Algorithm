import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] tree = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
        	tree[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(tree);
        int result = 0;
        for(int i = N-1 ; i > -1; i--) {
        	result = Math.max(result, tree[i] + N-i + 1);
        }
        System.out.println(result);
    }
}