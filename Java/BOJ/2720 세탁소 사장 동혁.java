import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); 
        for (int i = 0; i < T; i++) {
        	StringBuilder sb = new StringBuilder();
        	int n = Integer.parseInt(br.readLine());
        	sb.append(n/25).append(" ");
        	n -= 25 * (n/25);
        	sb.append(n/10).append(" ");
        	n -= 10 * (n/10);
        	sb.append(n/5).append(" ");
        	n -= 5 * (n/5);
        	sb.append(n).append(" ");
        	System.out.println(sb);
        }
    }
}