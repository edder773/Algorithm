import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	final static long mod = 1000000000;
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[][] num = new long[N+1][10];
        for(int i = 1; i < 10; i++) {
        	num[1][i] = 1;
        }
        for (int i = 2; i < N+1; i++) {
        	for (int j = 0; j < 10; j++) {
        		if (j == 0) {
        			num[i][j] = num[i-1][1] % mod;
        		}
        		else if(j == 9) {
        			num[i][j] = num[i-1][8] % mod;
        		}
        		else {
        			num[i][j] = (num[i-1][j-1] + num[i-1][j+1]) % mod;
        		}
        	}
        }
        long sum = 0;
        for (int i = 0; i < 10; i++) {
        	sum += num[N][i];
        }
        System.out.println(sum % mod);
    }
}