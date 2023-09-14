import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static int N, M;
	static int[][] fuel;
	static int[] move = new int[] {-1,0,1};
	static int find(int c, int r, int d, int now, int result) {
		if(c == N-1) {
			return Math.min(now, result);
		}
		for (int i : move) {
			if (i != d && c >= 0 && c < N && r+i >= 0 && r+i < M) {
				now = find(c+1, r+i, i, now, result + fuel[c+1][r+i]);
			}
		}
		return now;
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        fuel = new int[N][M];
        for(int i = 0 ; i < N; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	for(int j = 0 ; j < M ; j++) {
        		fuel[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        int result = Integer.MAX_VALUE;
        for (int i = 0 ; i < M; i++) {
        	result = find(0,  i,  2, result, fuel[0][i]);
        }
        System.out.println(result);
    }
}
