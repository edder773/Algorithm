import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] x = new int[n][];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            x[i] = new int[i + 1];
            for (int j = 0; j <= i; j++) {
                x[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < x[i].length; j++) {
                if (j == 0) {
                    x[i][j] += x[i - 1][j];
                } else if (j == x[i].length - 1) {
                    x[i][j] += x[i - 1][j - 1];
                } else {
                    x[i][j] += Math.max(x[i - 1][j], x[i - 1][j - 1]);
                }
            }
        }

        int maxValue = 0;
        for (int num : x[n - 1]) {
            maxValue = Math.max(maxValue, num);
        }

        System.out.println(maxValue);
    }
}