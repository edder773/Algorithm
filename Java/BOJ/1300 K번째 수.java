import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	int K = Integer.parseInt(br.readLine());
    	int start = 1;
    	int end = K;
    	int result = 0;
    	while (start <= end) {
    		int mid = (start+end)/2;
    		int count = 0;
    		for (int i = 1; i < N+1; i++) {
    			count += Math.min(mid/i, N);
    		}
    		if (count >= K) {
    			result = mid;
    			end = mid - 1;
    		}
    		else {
    			start = mid + 1;
    		}
    		
    	}
    	System.out.println(result);

    }
}