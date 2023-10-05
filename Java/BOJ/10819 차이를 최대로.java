import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	public static int N, result;
	public static int[] A, nums;
	public static boolean[] visited;
	
	public static void find(int n) {
		if (n == N) {
			int sum = 0;
			for (int i = 0; i < N-1; i++) {
				sum += Math.abs(nums[i] - nums[i+1]);
			}
			result = Math.max(result, sum);
			return;
		}
		for (int i = 0; i < N; i++) {
			if(!visited[i]) {
				nums[n] = A[i];
				visited[i] = true;
				find(n + 1);
				visited[i] = false;
			}
		}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        nums = new int[N];
        visited = new boolean[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
        	A[i] = Integer.parseInt(st.nextToken());
        }
        find(0);
        System.out.println(result);
    }
}