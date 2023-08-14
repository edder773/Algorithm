import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int M ;
	static int K ;
	static int[][] multi (int[][] a, int[][] b){
		int[][] X = new int[N][K];
		for(int i = 0 ; i < N; i ++) {
			for (int j= 0; j < K; j++) {
				for (int k = 0; k < M; k++) {
					X[i][j] += a[i][k] * b[k][j];
				}
			}
		}
		return X;
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int[][] A = new int[N][M];
        for (int i = 0 ; i < N; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	for (int j = 0; j < M; j++) {
        		A[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        st = new StringTokenizer(br.readLine()," ");
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        int[][] B = new int[M][K];
        for (int i = 0; i < M ; i ++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	for (int j = 0 ; j < K; j++) {
        		B[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        StringBuilder sb = new StringBuilder();
        int[][] result = multi(A,B);
        for(int i = 0; i < N; i ++ ) {
        	for (int j = 0; j < K; j++) {
        		sb.append(result[i][j] + " ");
        	}
        	sb.append("\n");
        }
        System.out.println(sb);
    }
}