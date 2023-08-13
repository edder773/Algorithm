import java.io.*;
import java.util.*;

public class Main {
	static long N;;
	static long K;
	final static long p = 1000000007;
	
	static long f(long n) {
		long x = 1;
		while (n > 1) {
			x = (x * n) % p;
			n --;
		}
		return x;
	}
	
	static long find(long x, long n) {
		if (n == 1) {
			return x % p;
		}
		long temp = find(x, n/2);
		if (n % 2 == 0) {
			return temp*temp %  p;
		}
		else {
			return( temp*temp %p)*x % p;
		}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Long.parseLong(st.nextToken());
        K = Long.parseLong(st.nextToken());
        long numer = f(N);
		long denom = f(K) * f(N - K) % p;	
	
		System.out.println(numer * find(denom, p - 2) % p);
    }
}