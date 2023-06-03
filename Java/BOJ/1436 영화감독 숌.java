import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int cnt = 0;
		int num = 0;
		while (cnt != N) {
			num ++;
			if (Integer.toString(num).contains("666")) {
				cnt ++;
			}
		}
		System.out.println(num);
	}
}