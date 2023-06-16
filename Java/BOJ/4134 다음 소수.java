import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static Boolean prime(long x) {
		if (x == 0 || x == 1) {
			return false;
		}
		for(int i = 2; i < (int)(Math.sqrt(x))+1; i++){
			if (x % i == 0) {
				return false;
			}
		}
		return true;
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int test = 0; test < T; test++) {
        	long n = Long.parseLong(br.readLine());
        	while (true) {
        		if (prime(n)) {
        			System.out.println(n);
        			break;
        		}
        		else {
        			n++;
        		}
        	}
        }
	}
}