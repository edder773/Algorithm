import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        String alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String N = st.nextToken();
        int B = Integer.parseInt(st.nextToken());
        int result = 0;
        int square = 0;
        for (int i = N.length()-1; i >= 0; i--) {
        	result += alpha.indexOf(N.charAt(i))*(Math.pow(B,square));
        	square++;
        }
        System.out.println(result);
    }
}