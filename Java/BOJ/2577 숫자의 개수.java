import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());
        String multi = Integer.toString(A*B*C);
        HashMap<Integer, Integer> x = new HashMap<Integer, Integer>();
        for(int i = 0; i < 10; i++) {
        	x.put(i, 0);
        }
        for(int i = 0; i < multi.length(); i++) {
        	int num = Integer.parseInt(String.valueOf(multi.charAt(i)));
        	x.put(num, x.get(num)+1);
        }
        for(int i = 0; i < 10; i++) {
        	System.out.println(x.get(i));
        }
    }
}