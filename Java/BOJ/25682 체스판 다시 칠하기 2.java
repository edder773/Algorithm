import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        char[][] chess = new char[N][M];
        for (int i = 0; i < N; i++) {
            chess[i] = br.readLine().toCharArray();
        }

        int[][] acc = new int[N + 1][M + 1];

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                if ((i + j) % 2 == 1) {
                    if (chess[i - 1][j - 1] == 'W') {
                        acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1];
                    } else {
                        acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + 1;
                    }
                } else {
                    if (chess[i - 1][j - 1] == 'B') {
                        acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1];
                    } else {
                        acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + 1;
                    }
                }
            }
        }

        int result_min = Integer.MAX_VALUE;
        int result_max = Integer.MIN_VALUE;

        for (int i = K; i <= N; i++) {
            for (int j = K; j <= M; j++) {
                result_min = Math.min(result_min, acc[i][j] - acc[i][j - K] - acc[i - K][j] + acc[i - K][j - K]);
                result_max = Math.max(result_max, acc[i][j] - acc[i][j - K] - acc[i - K][j] + acc[i - K][j - K]);
            }
        }

        int finalResult = Math.min(Math.min(result_max, result_min), Math.min(K * K - result_max, K * K - result_min));
        System.out.println(finalResult);
    }
}