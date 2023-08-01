import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] x = new int[N];
        for(int i = 0 ; i < N; i++) {
        	x[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(x);
        int sum = 0;
        for(int i = 1; i < N; i++) {
        	x[i] += x[i-1];
        	sum += x[i];
        }
        System.out.println(sum+x[0]);
    }
}