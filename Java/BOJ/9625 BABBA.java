import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        int a = 1, b = 0;
        for (int i = 0 ; i < K; i++) {
        	int temp = a;
        	a = b;
        	b = temp+b;
        }
        System.out.println(a + " " + b);
    }
}