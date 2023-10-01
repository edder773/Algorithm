import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        for (int i = (N+1)/3; i < (N+1)/2; i++) {
        	result += (3*i - N + 2)/2;
        }
        System.out.println(result);
    }
}