import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        int[] A = new int[N];
        for(int i = 0; i< N; i++) {
        	A[i] = Integer.parseInt(st.nextToken());
        }
        int left = 0;
        int right = 0;
        int result = 0;
        while(right <= N) {
        	int sum = 0;
        	for (int i = left; i < right; i++) {
        		sum += A[i];
        	}
        	if(sum == M) {
        		result++;
        		left++;
        	}
        	else if(sum < M) {
        		right++;
        	}
        	else {
        		left++;
        	}
        }
        System.out.println(result);
    }
}