import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int score = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        int[] num = new int[N];
        if (N == 0) {
        	System.out.println(1);
        }
        else {
        	st = new StringTokenizer(br.readLine(), " ");
        	for(int i = 0 ; i < N; i++) {
        		num[i] = Integer.parseInt(st.nextToken());
        	}
        	if(N == P && num[N-1] >= score) {
        		System.out.println(-1);
        	}
        	else {
        		int result = N + 1;
        		for (int i =0 ; i < N; i ++) {
        			if (num[i] <= score) {
        				result = i+1;
        				break;
        			}
        		}
        		System.out.println(result);
        	}
        }
    }
}
