import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t= 0; t< T; t++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int N = Integer.parseInt(st.nextToken());
        	int M = Integer.parseInt(st.nextToken());
        	int[] A = new int[N];
        	int[] B = new int[M];
        	st = new StringTokenizer(br.readLine());
        	for (int i = 0; i < N; i++) {
        		A[i] = Integer.parseInt(st.nextToken());
        	}
        	st = new StringTokenizer(br.readLine());
        	for (int i = 0 ; i < M; i++) {
        		B[i] = Integer.parseInt(st.nextToken());
        	}
        	
        	Arrays.sort(B);
        	int result = 0;
        	for (int i : A) {
        		int start = 0, end = M-1;
        		int temp = -1;
        		while (start <= end) {
        			int mid = (start + end) / 2;
        			if (B[mid] < i) {
        				start = mid + 1;
        				temp = mid;
        			}
        			else {
        				end = mid - 1;
        			}
        		}
        		result += temp + 1;
        	}
        	System.out.println(result);
        }
    }
}