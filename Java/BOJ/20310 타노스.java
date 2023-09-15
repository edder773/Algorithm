import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static int count(String S, char n) {
		int result = 0;
		for (int i = 0 ; i < S.length(); i++) {
			if (S.charAt(i) == n) {
				result++;
			}
		}
		return result;
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int N = S.length();
        char[] C = new char[N];
        for(int i = 0; i < N; i++) {
        	C[i] = S.charAt(i);
        }
        
        int zero = count(S,'0')/2;
        int one = count(S, '1')/2;
        for (int i = N-1; i > -1; i--) {
        	if (zero > 0 && C[i] == '0') {
        		C[i] = 'x';
        		zero--;
        	}
        }
        for (int i = 0; i < N; i++) {
        	if( one > 0 && C[i] == '1') {
        		C[i] = 'x';
        		one--;
        	}
        }
        String result = "";
        for (char i : C) {
        	if(i != 'x') {
        		result += i;
        	}
        }
        System.out.println(result);
    }
}