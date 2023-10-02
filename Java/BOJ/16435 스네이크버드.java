import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int[] h = new int[N];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0 ; i < N; i++) {
        	h[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(h);
        for (int i : h) {
        	if (L >= i) {
        		L++;
        	}
        }
        System.out.println(L);
    }
}