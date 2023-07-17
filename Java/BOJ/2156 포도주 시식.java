import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] wine = new int[10001];
        for(int i = 0; i < N; i++) {
        	wine[i] = Integer.parseInt(br.readLine());
        }
        int[] dp = new int[10001];
        dp[0] = wine[0];
        dp[1] = wine[0] + wine[1];
        dp[2] = Math.max(Math.max(wine[2] + wine[0], wine[2] + wine[1]), dp[1]);
        for (int i = 3; i < N; i++) {
        	dp[i] = Math.max(Math.max(wine[i] + dp[i-2], wine[i] + wine[i-1]+dp[i-3]), dp[i-1]);
        }
        int maxValue = 0;
        for (int i = 0; i < N+1; i++) {
        	if (maxValue < dp[i]) {
        		maxValue = dp[i];
        	}
        }
        System.out.println(maxValue);
    }
}