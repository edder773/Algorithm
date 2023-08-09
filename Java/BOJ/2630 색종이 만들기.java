import java.io.*;
import java.util.*;

public class Main {
	static int[][] paper;
	static int[] result = {0,0};
	static void div(int y, int x, int n) {
		int color = paper[y][x];
		for (int i = y; i < y+n; i++) {
			for (int j = x; j < x+n; j++) {
				if (color != paper[i][j]) {
					int m = n/2;
					div(y, x , m);
					div(y, x + m, m);
					div(y + m, x, m);
					div(y + m, x + m , m);
					return;
				}
			}
		}
		if (color == 0) {
			result[0]++;
		}
		else {
			result[1]++;
		}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        paper = new int[N][N];
        for (int i = 0 ; i < N; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine(), " " );
        	for (int j = 0; j < N; j++) {
        		paper[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        div(0, 0 , N);
        System.out.println(result[0]);
        System.out.println(result[1]);
    }
}