import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int result = Integer.MIN_VALUE;
		int index = 0;
		for (int i = 1; i < 10; i++) {
			int x = Integer.parseInt(br.readLine());
			if (result < x) {
				result = x;
				index = i;
			}
		}
		System.out.println(result);
		System.out.println(index);
	}
}