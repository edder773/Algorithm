import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] P = new int[M];
        for(int i = 0 ; i < M; i++) {
        	P[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(P);
        int result = 0;
        int cost = 0;
        for (int i = 0 ; i < M; i++) {
        	int temp = M - i;
        	if (temp <= N && P[i] * temp > result) {
        		result = temp*P[i];
        		cost = P[i];
        	}
        }
        System.out.print(cost + " " + result);
    }
}