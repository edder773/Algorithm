import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int n = Integer.parseInt(br.readLine());
            StringBuilder sb = new StringBuilder();
            if (n == -1) {
                break;
            }
            int sum = 0;
            for (int i = 1; i < n; i++) {
                if (n % i == 0) {
                    sb.append(i).append(" + ");
                    sum += i;
                }
            }
            if (sb.length() > 0) {
                sb.delete(sb.length() - 2, sb.length());
            }
            
            if (sum == n) {
                System.out.printf("%d = ", n);
                System.out.println(sb);
            }
            else {
            	System.out.printf("%d is NOT perfect.\n", n);
            }
        }
    }
}