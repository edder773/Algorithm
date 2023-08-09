import java.io.*;
import java.util.*;

public class Main {    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        long[] line = new long[N-1];
        for (int i = 0; i < N-1; i ++) {
        	line[i] = Integer.parseInt(st.nextToken());
        }
        long[] price = new long[N];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < N; i++) {
        	price[i] = Integer.parseInt(st.nextToken());
        }
        
        long a = line[0] * price[0];
        long b = price[0];
        
        for (int i = 1; i < N-1; i++) {
        	if (b > price[i]) {
        		b = price[i];
        	}
        	a += b *line[i];
        }
        System.out.println(a);
    }
}