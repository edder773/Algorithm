import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[][] paper;
	static int[] result = {0, 0, 0};
	public static void div(int y, int x, int n ) {
		int num = paper[y][x];
		for(int i = y; i < y + n; i++) {
			for (int j = x; j < x + n; j++) {
				if (num != paper[i][j]) {
					int m = n/3;
					div(y, x, m);
					div(y, x + m, m);
					div(y, x + 2*m, m);
					div(y + m, x, m);
					div(y + m, x + m, m);
					div(y + m, x + 2*m, m);
					div(y + 2*m, x, m);
					div(y + 2*m, x + m, m);
					div(y + 2*m, x + 2*m, m);
					return;
				}
			}
		}
		if (num == -1) {
			result[0] += 1;
		}
		else if (num == 0) {
			result[1] += 1;
		}
		else {
			result[2] += 1;
		}
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        paper = new int[N][N];
        for (int i = 0 ; i < N; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        	for (int j = 0 ; j < N; j++) {
        		paper[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        div(0,0,N);
        System.out.println(result[0]);
        System.out.println(result[1]);
        System.out.println(result[2]);
    }
}