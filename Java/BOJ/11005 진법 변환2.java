import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        String alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int N = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        String result = "";
        while (N > 0) {
        	result = alpha.charAt(N%B) + result;
        	N /= B;
        }
        System.out.println(result);
    }
}