import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0 ; i < n; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	long a = Integer.parseInt(st.nextToken());
        	long b = Integer.parseInt(st.nextToken());
        	long num = a*b;
        	while(b > 0) {
        		long mod = b;
        		b = a % b;
        		a = mod;
        	}
        	System.out.println(num/a);
        }
    }
}