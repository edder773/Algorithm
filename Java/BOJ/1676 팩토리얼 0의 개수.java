import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        BigInteger factorial = BigInteger.ONE;
        
        for (int i = 1; i <= N; i++) {
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }
        String x = factorial.toString();
        int result = 0;
        for (int i = x.length()-1; i > -1; i--) {
        	if (x.charAt(i) == '0') {
        		result++;
        	}
        	else if (x.charAt(i) != '0') {
        		break;
        	}
        }
        System.out.println(result);
    }
}