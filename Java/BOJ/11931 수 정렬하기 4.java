import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Integer[] x = new Integer[N];
        for (int i = 0; i < N; i++) {
        	x[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(x, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for(int i : x) {
        	sb.append(i).append('\n');
        }
        System.out.println(sb);
    }
}