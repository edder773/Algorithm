import java.util.*;
import java.io.*;

public class Main {
	static int[] A;
	static int max = Integer.MIN_VALUE;
	static int min = Integer.MAX_VALUE;
	static int N, plus, minus, multi, divide;
	public static void find(int n, int result) {
		if (n == N) {
			max = Math.max(max, result);
			min = Math.min(min, result);
			return;
		}
		if (plus > 0) {
			plus -= 1;
			find(n+1, result + A[n]);
			plus += 1;
		}
		if (minus > 0) {
			minus -= 1;
			find(n+1, result - A[n]);
			minus += 1;
		}
		if (multi > 0) {
			multi -= 1;
			find(n+1, result * A[n]);
			multi += 1;
		}
		if (divide > 0) {
			divide -= 1;
			find(n+1, (int)(result / A[n]));
			divide += 1;
		}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        for (int i = 0; i < N; i++) {
        	A[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine()," ");
        plus = Integer.parseInt(st.nextToken());
        minus = Integer.parseInt(st.nextToken());
        multi = Integer.parseInt(st.nextToken());
        divide = Integer.parseInt(st.nextToken());
        find(1, A[0]);
        System.out.println(max);
        System.out.println(min);
    }
}