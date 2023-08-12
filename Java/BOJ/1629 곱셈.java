import java.io.*;
import java.util.*;

public class Main {
	static long A;
	static long B;
	static long C;
	
	static long find(long x, long n) {
        if (n == 1) {
            return x;
        }
        long temp = find(x, n / 2);
        if (n % 2 == 0) {
            return (temp * temp) % C;
        } else {
            return (temp * temp % C) * x % C;
        }
    }
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());
        C = Long.parseLong(st.nextToken());
        System.out.println(find(A,B)%C);
    }
}