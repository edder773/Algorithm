import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int result = 1;
        int count = 0;
        for (int i = N; i > N-K; i--) {
        	result *= i;
        	count++;
        }
        int x = 1;
        for (int j = 1; j < count+1; j++) {
        	x *= j;
        }
        System.out.println(result/x);
	}
}