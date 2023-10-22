import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = 1000001;
        long[] fn = new long[num];
        long[] gn = new long[num];
        for (int i = 0; i < num; i++) {
        	fn[i] = 1;
        }
        for (int i = 2; i < num; i++) {
        	int j = 1;
        	while (i*j < num) {
        		fn[i*j] += i;
        		j++;
        	}
        }
        
        for (int i = 1; i < num; i++) {
        	gn[i] = gn[i-1] + fn[i];
        }
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < T; i++) {
        	int n = Integer.parseInt(br.readLine());
        	sb.append(gn[n]).append('\n');
        }
        System.out.println(sb);
    }
}