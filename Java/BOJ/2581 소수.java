import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main{
	
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
		
		
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		ArrayList<Integer> x = prime(M,N);
		int result = 0;
		for(int i : x) {
			result += i;
		}
		if (x.size() > 0) {
			System.out.println(result);
			System.out.println(x.get(0));
		}
		else {
			System.out.println(-1);
		}
	}
}