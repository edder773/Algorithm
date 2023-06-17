import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static boolean[] prime(int n){
		boolean[] isprime = new boolean[n+1];
		for(int i = 0; i <= n; i++){
			isprime[i] = true;
		}
		isprime[0] = isprime[1] = false;
		for (int i = 2; i*i <= n; i++) {
			if(isprime[i]) {
				for (int j = i*i; j <= n; j += i) {
					isprime[j] = false;
				}
			}
		}
		
		return isprime;
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean[] primes = prime(1000000);
        int T = Integer.parseInt(br.readLine());
        for (int cases = 0; cases < T; cases++) {
        	int result = 0;
        	int N = Integer.parseInt(br.readLine());
        	for(int i = 0; i< N/2+1; i++) {
        		if (primes[i] && primes[N-i]) {
        			result++;
        		}
        	}
        	System.out.println(result);
        }
	}
}