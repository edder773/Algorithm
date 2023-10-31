import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Integer[] milk = new Integer[N];
        for (int i = 0 ; i < N; i++) {
        	milk[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(milk, Collections.reverseOrder());
        int result = 0;
        for (int i = 0; i < N; i++) {
        	if((i+1) % 3 > 0) {
        		result += milk[i];
        	}
        }
        System.out.println(result);
    }
}