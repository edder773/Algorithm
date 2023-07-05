import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	private static StringBuilder sb = new StringBuilder();
	
    public static void hanoi(int a, int b, int c, int d) {
    	if(d == 0)
    		return;
    	hanoi(a, c, b, d-1);
    	sb.append(a).append(" ").append(c).append("\n");
    	hanoi(b, a, c , d-1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        System.out.println((int)Math.pow(2, N)-1);
        hanoi(1, 2, 3, N);
        System.out.println(sb);
    }
}