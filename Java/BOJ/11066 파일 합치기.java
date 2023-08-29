import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
        	int K = Integer.parseInt(br.readLine());
        	int[] size = new int[K+1];
        	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        	for (int i = 1; i < K+1; i++) {
        		size[i] = Integer.parseInt(st.nextToken());
        	}
        	int[] sized = new int[K+1];
        	int[][] dp = new int[K+1][K+1];
        	for (int i = 1; i < K+1; i++) {
        		sized[i] = sized[i-1] + size[i];
        	}
        	
        	for (int i = 2; i <= K; i++) {
                for (int j = 1; j <= K + 1 - i; j++) {
                    dp[j][j + i - 1] = Integer.MAX_VALUE;
                    for (int k = 0; k < i - 1; k++) {
                        dp[j][j + i - 1] = Math.min(dp[j][j + i - 1], dp[j][j + k] + dp[j + k + 1][j + i - 1] + (sized[j + i - 1] - sized[j - 1]));
                    }
                }
            }
            
            System.out.println(dp[1][K]);
        }
    }
}
