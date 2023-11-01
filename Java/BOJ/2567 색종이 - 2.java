import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] paper = new int[102][102];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            for (int j = a; j < a + 10; j++) {
                for (int k = b; k < b + 10; k++) {
                    paper[j][k] = 1;
                }
            }
        }

        int[][] move = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int result = 0;

        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if (paper[i][j] == 1) {
                    for (int[] dir : move) {
                        int dy = dir[0];
                        int dx = dir[1];
                        int ny = i + dy;
                        int nx = j + dx;
                        if (paper[ny][nx] == 0) {
                            result++;
                        }
                    }
                }
            }
        }

        System.out.println(result);
    }
}