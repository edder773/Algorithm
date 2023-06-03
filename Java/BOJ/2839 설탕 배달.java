import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int result = 0;
		while (true) {
			if (N % 5 == 0) {
				result += N / 5;
				System.out.println(result);
				break;
			}
			N -= 3;
			result ++;
			if (N < 0) {
				System.out.println(-1);
				break;
			}
		}
	}
}