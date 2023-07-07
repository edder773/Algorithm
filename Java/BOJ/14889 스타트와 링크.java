import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] S;
    static int[] visited;
    static int result = Integer.MAX_VALUE;

    public static void team(int a, int n) {
        if (a == N / 2) {
            int start = 0;
            int link = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visited[i] > 0 && visited[j] > 0) {
                        start += S[i][j];
                    } else if (visited[i] == 0 && visited[j] == 0) {
                        link += S[i][j];
                    }
                }
            }
            result = Math.min(result, Math.abs(start - link));
            return;
        } else {
            for (int i = n; i < N; i++) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    team(a + 1, i + 1);
                    visited[i] = 0;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        S = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                S[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        visited = new int[N];
        team(0, 0);
        System.out.println(result);
    }
}