import java.io.*;
import java.util.*;

public class Main {    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] S = br.readLine().split("-");
        int[] x = new int[S.length];
        
        for (int i = 0; i < S.length; i++) {
        	String[] y = S[i].split("\\+");
        	int cnt = 0;
        	for (String j : y ) {
        		cnt += Integer.parseInt(j);
        	}
        	x[i] = cnt;
        }
        
        int result = x[0];
        for (int i = 1 ; i < x.length; i++) {
        	result -= x[i];
        }
        System.out.println(result);
    }
}