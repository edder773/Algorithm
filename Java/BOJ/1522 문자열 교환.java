import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	
	static int count(String s, char x) {
		int num = 0;
		for (int i = 0; i < s.length(); i++) {
			if(s.charAt(i) == x) {
				num++;
			}
		}
		return num;
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int a = count(S,'a');
        if (a > 0) {
        	S += S.substring(0,a-1);
        	int result = Integer.MAX_VALUE;
        	for (int i = 0 ; i < S.length() - (a-1); i++) {
        		int b = count(S.substring(i, i+a),'b');
        		result = Math.min(result, b);
        	}
        	System.out.println(result);        	
        }
        else {
        	System.out.println(0);
        }
    }
}
