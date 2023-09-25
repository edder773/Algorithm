import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
        	int N = Integer.parseInt(br.readLine());
        	int a = 1;
        	int b = 0;
        	for (int j = 0; j < N; j++) {
        		int temp = a;
        		a = b;
        		b = temp+b;
        	}
        	sb.append(a).append(" ").append(b).append("\n");
        }
        System.out.println(sb);
    }
}