import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        int num = 64;
        int result = 0;
        while (num > 0) {
        	int a = X / num;
        	result += a;
        	X -= num * a;
        	num /= 2;
        }
        System.out.println(result);
    }
}