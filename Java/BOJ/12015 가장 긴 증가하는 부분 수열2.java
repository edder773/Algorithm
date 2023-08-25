import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    	int[] A = new int[N];
    	ArrayList <Integer> result = new ArrayList<>();
    	result.add(0);
    	for (int i = 0; i < N; i ++) {
    		A[i] = Integer.parseInt(st.nextToken());
    	}
    	
    	for(int i : A) {
    		if (result.get(result.size()-1) < i) {
    			result.add(i);
    		}
    		else {
    			int left = 0;
    			int right = result.size();
    			while (left < right) {
    				int mid = (left + right)/2;
    				if (result.get(mid) < i) {
    					left = mid + 1;
    				}
    				else {
    					right = mid;
    				}
    			}
    			result.set(right, i);
    		}
    	}
    	System.out.println(result.size() - 1);
    }
}