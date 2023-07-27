import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] temp = new int[N+1];
        ArrayList <Integer> x = new ArrayList<>();
        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 1; i < N+1; i++) {
        	temp[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 1; i < N+1; i++) {
        	temp[i] += temp[i-1];
        }
        for (int j = K; j < N+1; j++) {
        	x.add(temp[j] - temp[j-K]);        	
        }
        int result = Collections.max(x);
        System.out.println(result);
	}
}