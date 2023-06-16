import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static ArrayList<Integer> prime(int a, int b){
		boolean[] prime = new boolean[b+1];
		for(int i = 0; i <= b; i++){
			prime[i] = true;
		}
		prime[0] = prime[1] = false;
		for (int i = 2; i*i <= b; i++) {
			if(prime[i]) {
				for (int j = i*i; j <= b; j += i) {
					prime[j] = false;
				}
			}
		}
		
		ArrayList<Integer> primes = new ArrayList<>();
		for (int i = a; i <= b; i++) {
			if(prime[i]) {
				primes.add(i);
			}
		}
		
		return primes;
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        ArrayList<Integer> nums = prime(M,N);
        for(int i = 0; i<nums.size(); i++) {
        	System.out.println(nums.get(i));
        }
	}
}