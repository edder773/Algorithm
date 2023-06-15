import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static int GCD(int a, int b) {
		if (a % b == 0) {
			return b;
		}
		return GCD(b, a%b);
	}
	public static long LCM (long a, long b) {
		int gcd = GCD((int)a, (int)b);
		if (gcd == 0) {
			return 0;
		}
		return Math.abs(a*b/gcd);
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        long A = Integer.parseInt(st.nextToken());
        long B = Integer.parseInt(st.nextToken());
        long lcm = LCM(A,B);
        System.out.println(lcm);
	}
}