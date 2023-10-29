import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int result = 0;
        for (int i = 0; i < S.length()-1; i++) {
        	if(S.charAt(i) != S.charAt(i+1)) {
        		result++;
        	}
        }
        System.out.println((result+1)/2);
    }
}