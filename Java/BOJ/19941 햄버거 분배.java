import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        char[] table = new char[N];
        String S = br.readLine();
        for(int i = 0 ; i < N; i++) {
        	table[i] = S.charAt(i);
        }
        int result = 0;
        for(int i = 0; i < N; i++) {
        	if(table[i] == 'P') {
        		for (int x = Math.max(i-K, 0); x < Math.min(i+K+1, N); x++) {
        			if(table[x] == 'H') {
        				table[x] = 'X';
        				result++;
        				break;
        			}
        		}
        	}
        }
        System.out.println(result);
    }
}