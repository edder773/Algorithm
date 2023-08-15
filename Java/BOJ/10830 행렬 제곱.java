import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static long B ;

	static long[][] multi (long[][] a, long[][] b){
		long[][] X = new long[N][N];
		for(int i = 0 ; i < N; i ++) {
			for (int j= 0; j < N; j++) {
				for (int k = 0; k < N; k++) {
					X[i][j] += a[i][k] * b[k][j] % 1000;
				}
			}
		}
		return X;
	}
	
	static long[][] square(long[][] x, long n) {
		if (n == 1) {
			return x;
		}
		long[][] temp = square(x, n/2);
		if (n % 2 == 0) {
			return multi(temp, temp);
		}
		else {
			return multi(multi(temp, temp), x);
		}
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        B = Long.parseLong(st.nextToken());
        long[][] A = new long[N][N];
        for (int i = 0 ; i < N; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	for (int j = 0; j < N; j++) {
        		A[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        StringBuilder sb = new StringBuilder();
        long[][] result = square(A, B);
        for(int i = 0; i < N; i ++ ) {
        	for (int j = 0; j < N; j++) {
        		result[i][j] %= 1000;
        		sb.append(result[i][j] + " ");
        	}
        	sb.append("\n");
        }
        System.out.println(sb);
    }
}