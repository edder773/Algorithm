import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] dp = new long[1000001];
        dp[1] = 1;
        for (int i = 2; i < 1000001; i++) {
        	dp[i] = (dp[i-1] + dp[i-2]) % 1000000000;
        }
        if (n % 2 == 0 && n < 0) {
        	System.out.println(-1);
        }
        else if (n == 0) {
        	System.out.println(0);
        }
        else {
        	System.out.println(1);
        }
        System.out.println(dp[Math.abs(n)]);
    }
}