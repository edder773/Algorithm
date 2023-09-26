import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	public static List<Integer> prime(int n) {
		boolean[] arr = new boolean[n];
		for (int i = 0; i < n; i++) {
			arr[i] = true;
		}
		int m = (int) Math.sqrt(n);
		for (int i = 2; i < m+1; i++) {
			if(arr[i]) {
				for(int j = i + i; j < n; j+= i) {
					arr[j] = false;
				}
			}
		}
		
		List<Integer> primes = new ArrayList<>();
		for(int i = 2; i < n; i++) {
			if (arr[i]) {
				primes.add(i);
			}
		}
		return primes;
	}
	
	public static boolean palindrome (String n) {
		for (int i = 0; i < n.length(); i++) {
			if (n.charAt(i) != n.charAt(n.length()-1-i)) {
				return false;
			}
		}
		return true;
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List <Integer> primes= prime(1030000);
        for (int i = 0; i < primes.size(); i++) {
        	if(primes.get(i) >= N && palindrome(primes.get(i).toString())) {
        		System.out.println(primes.get(i));
        		break;
        	}
        }
    }
}