import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		long n = Integer.parseInt(br.readLine());
		long sum = 0;
		for (int i = 0; i < n; i++) {
			sum += i;
		}
		System.out.println(sum);
		System.out.println(2);
	}
}