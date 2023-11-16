import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = 0;
        int i = 0;
        while(true) {
        	if (n % 5 == 0) {
        		result += n/5;
        		break;
        	}
        	else {
        		n -= 2;
        		result++;
        	}
        	
        	if (n < 0) {
        		break;
        	}
        }
        if (n < 0) {
        	result = -1;
        }
        System.out.println(result);
    }
}