import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        for(int i = 0; i < N; i++) {
        	String x = br.readLine();
        	if ((x+x).contains(S)) {
        		result++;
        	}
        }
        System.out.println(result);
    }
}