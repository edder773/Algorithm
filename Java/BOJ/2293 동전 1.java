import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] coins = new int[n];
        for (int i = 0 ; i < n; i++) {
        	coins[i] = Integer.parseInt(br.readLine());
        }
        long[] dp = new long[k+1];
        dp[0] = 1;
        for (int i : coins) {
            for (int j = i; j <= k; j++) {
                if (j - i >= 0) {
                    dp[j] += dp[j - i];
                }
            }
        }
        System.out.println(dp[k]);
    }
}
