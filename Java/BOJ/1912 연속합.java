import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int[] x = new int[N];
        for (int i = 0; i < N; i++) {
        	x[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 1; i < N; i++) {
        	x[i] = Math.max(x[i], x[i] + x[i-1]);
        }
        System.out.println(Arrays.stream(x).max().getAsInt());
    }
}