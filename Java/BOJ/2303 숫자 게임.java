import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] students = new int[N][5];
        int num = 0, winner = 0;
        for (int i = 0 ; i < N; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	for(int j = 0 ; j < 5; j++) {
        		students[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < 5; j++) {
                for (int k = j + 1; k < 5; k++) {
                    for (int l = k + 1; l < 5; l++) {
                        int sum = (students[i][j] + students[i][k] + students[i][l]) % 10;
                        if (num <= sum) {
                            num = sum;
                            winner = i + 1;
                        }
                    }
                }
            }
        }
        System.out.println(winner);
    }
}