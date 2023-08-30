import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] A = new int[N][2];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            A[i][0] = Integer.parseInt(st.nextToken());
            A[i][1] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        
        for (int i = 0; i < N; i++) {
            dp[i][i] = 0;
        }
        
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < N - i; j++) {
                for (int k = j; k < i + j; k++) {
                    int a = j, b = k, c = i + j;
                    dp[a][c] = Math.min(
                        dp[a][c],
                        dp[a][b] + dp[b + 1][c] + A[a][0] * A[b][1] * A[c][1]
                    );
                }
            }
        }
        
        System.out.println(dp[0][N - 1]);
    }
}