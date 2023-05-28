import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int i = 2;
		while(N > i) {
			if( N % i == 0) {
				N /= i;
				System.out.println(i);
			}
			else {
				i++;
			}
		}
		if (N > 1) {
			System.out.println(N);			
		}
	}
}