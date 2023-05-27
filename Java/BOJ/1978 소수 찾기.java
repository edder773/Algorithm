import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static boolean[] prime;
	
	static void isprime(int n) {
		prime = new boolean[n+1];
		for(int i = 0; i < prime.length; i++) {
			prime[i] = true;
		}
		prime[0] = prime[1] = false;
		for(int i = 2; i <= Math.sqrt(n); i++) {
			if(prime[i]) {
				for(int j = i*i; j <= n; j += i) {
					prime[j] = false;
				}
			}
		}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int result = 0;
        for (int i = 0; i < N; i++) {
        	int num = Integer.parseInt(st.nextToken());
        	isprime(num);
        	if(prime[num]) {
        		result++;
        	}
        }
        System.out.println(result);
    }
}