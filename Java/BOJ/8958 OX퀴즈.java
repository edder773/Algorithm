import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int test = 0; test < T; test++) {
			String S = br.readLine();
			int cnt = 0;
			int result = 0;
			for (int i = 0; i < S.length(); i++) {
				if (S.charAt(i) == 'O') {
					cnt ++;
					result += cnt;
				}
				else if (S.charAt(i) == 'X') {
					cnt = 0;
				}
			}
			System.out.println(result);
		}
	}
}