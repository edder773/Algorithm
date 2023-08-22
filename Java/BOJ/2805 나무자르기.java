import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static long[] tree;
	static int N;
	static long M;
	static long search() {
		long start = 1;
		long end = tree[N-1];
		while (start <= end) {
			long mid = (start + end)/2;
			long num = 0;
			for (int i = 0; i< N; i++) {
				if (tree[i] > mid) {
					num += tree[i] - mid;					
				}
			}
			if (num >= M) {
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
        N = Integer.parseInt(st.nextToken());
        M = Long.parseLong(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        tree = new long[N];
        for(int i = 0; i < N; i++) {
        	tree[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(tree);
        System.out.println(search());
    }
}