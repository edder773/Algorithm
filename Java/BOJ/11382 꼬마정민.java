import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		Long A = Long.parseLong(input[0]);
		Long B = Long.parseLong(input[1]);
		Long C = Long.parseLong(input[2]);
		
		System.out.println(A+B+C);
	}
}