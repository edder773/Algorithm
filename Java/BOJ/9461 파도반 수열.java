import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        long[] p = new long[101];
        p[0] = 1;
        p[1] = 1;
        p[2] = 1;
        p[3] = 2;
        p[4] = 2;
        for(int i = 0; i < 95; i++) {
        	p[i+5] = p[i] + p[i+4];
        }
        for (int i = 0; i < T; i++) {
        	int N = Integer.parseInt(br.readLine());
        	System.out.println(p[N-1]);
        }
    }
}