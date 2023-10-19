import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String A = st.nextToken();
        String B = st.nextToken();
        int n = A.length();
        int m = B.length();
        int result = Integer.MAX_VALUE;
        for(int i = 0; i < m-n+1; i++) {
        	int temp = 0;
        	for (int j = 0; j < n; j++) {
        		if(A.charAt(j) != B.charAt(i+j)) {
        			temp++;
        		}
        	}
        	result = Math.min(result, temp);
        }
        System.out.println(result);
    }
}