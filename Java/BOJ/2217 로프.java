import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] weight = new int[N];
        for (int i = 0; i < N; i++) {
        	int num = Integer.parseInt(br.readLine());
        	weight[i] = num;
        }
        Arrays.sort(weight);
        int result = 0;
        for (int i = 0 ; i < N; i++) {
        	result = Math.max(result, weight[N-1-i]*(i+1));
        }
        System.out.println(result);
    }
}