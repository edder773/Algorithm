import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static long[] x;
	static int K;
	static int N;
	static long search() {
		long start = 1;
		long end = x[K-1];
		while (start <= end) {
			long mid = (start + end)/2;
			long num = 0;
			for (int i = 0; i< K; i++) {
				num += x[i]/mid;
			}
			if (num >= N) {
				start = mid + 1;
			}
			else {
				end = mid - 1;
			}
		}
		return end;
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        x = new long[K];
        for (int i = 0 ; i < K; i++) {
        	x[i] = Long.parseLong(br.readLine());
        }
        Arrays.sort(x);;
        System.out.println(search());
    }
}