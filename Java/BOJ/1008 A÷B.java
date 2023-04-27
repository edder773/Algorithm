import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		double a = Integer.parseInt(input[0]);
		double b = Integer.parseInt(input[1]);
		System.out.println(a/b);
	}
}