import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] A = new int[N+1];
        int[] cost = new int[N+1];
        st = new StringTokenizer(br.readLine(), " " );
        for (int i = 1; i <= N; i++) {
        	A[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine(), " ");
        int sum = 0;
        for (int i = 1; i <= N; i++) {
        	cost[i] = Integer.parseInt(st.nextToken());
        	sum += cost[i];
        }
        
        int[][] dp = new int[N+1][sum + 1];
        int result = sum;
        
        for(int i = 1; i < N+1; i++) {
        	for(int j = 1; j < sum+1; j++) {
        		if(j < cost[i]) {
        			dp[i][j] = dp[i-1][j];
        		}
        		else {
        			dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j -cost[i]] + A[i]);
        		}
        		
        		if (dp[i][j] >= M) {
        			result = Math.min(result, j);
        		}
        	}
        }
        System.out.println(result);
    }
}
