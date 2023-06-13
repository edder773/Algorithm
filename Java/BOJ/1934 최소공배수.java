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
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	int A = Integer.parseInt(st.nextToken());
        	int B = Integer.parseInt(st.nextToken());
        	int gcd = GCD(A,B);
        	System.out.println(A*B / gcd);
        }
	}
}