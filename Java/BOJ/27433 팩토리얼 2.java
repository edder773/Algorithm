import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static long factorial(long n) {
		if (n == 0) {
			return 1;
		}
		return factorial(n-1) * n;
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        long result = factorial(N);
        System.out.println(result);
    }
}